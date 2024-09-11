import locale
import logging
from datetime import datetime

from sqlmodel import func, select

from bcdio.database import get_session
from bcdio.models import Conta, Movimentacao, Usuario

# Configuração de localização e logging
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
logging.basicConfig(
    filename="errors.log",
    format="%(asctime)s %(message)s",
    encoding="utf-8",
    level=logging.ERROR,
)


class SistemaBancario:
    def __init__(self):
        self.session = get_session()  # Utilize a sessão do banco de dados
        self.limite = 500.0

    def criar_usuario(self, nome, cpf, data_nascimento, endereco):
        try:
            logradouro = endereco["logradouro"]
            numero = endereco["numero"]
            bairro = endereco["bairro"]
            cidade = endereco["cidade"]
            estado = endereco["estado"]
        except KeyError as e:
            raise ValueError(f"Faltando informações no endereço: {e}")

        with self.session as session:
            # Verifica se o CPF já está cadastrado
            if session.exec(select(Usuario).where(Usuario.cpf == cpf)).first():
                raise ValueError("CPF já cadastrado.")

            # Cria o novo usuário
            novo_usuario = Usuario(
                nome=nome,
                cpf=cpf,
                data_nascimento=data_nascimento,
                logradouro=logradouro,
                numero=numero,
                bairro=bairro,
                cidade=cidade,
                estado=estado,
            )
            session.add(novo_usuario)
            session.commit()

            # O novo usuário deve estar dentro da sessão
            session.refresh(novo_usuario)
            return novo_usuario

    def excluir_usuario(self, cpf):
        with self.session as session:
            # Verifica se o usuário existe
            usuario = session.exec(select(Usuario).where(Usuario.cpf == cpf)).first()
            if not usuario:
                raise ValueError(f"Usuário com CPF {cpf} não encontrado.")

            # Verifica se o usuário possui contas associadas
            contas = session.exec(
                select(Conta).where(Conta.usuario_id == usuario.id)
            ).all()
            if contas:
                # Exclui todas as contas associadas
                for conta in contas:
                    session.delete(conta)

            # Exclui o usuário
            session.delete(usuario)
            session.commit()
            return f"Usuário com CPF {cpf} excluído com sucesso!"

    def criar_conta(self, cpf):
        with self.session as session:
            # Verifica se o usuário com o CPF informado existe
            usuario = session.exec(select(Usuario).where(Usuario.cpf == cpf)).first()
            if not usuario:
                raise ValueError(f"Usuário com CPF {cpf} não encontrado.")

            # Obtém o número da conta máximo atual
            resultado = session.exec(select(func.max(Conta.numero))).first()
            ultimo_numero = resultado if resultado is not None else 0
            novo_numero_conta = ultimo_numero + 1

            # Cria a nova conta com o número incrementado
            nova_conta = Conta(
                numero=novo_numero_conta,
                agencia="0001",
                saldo=0.0,
                usuario_id=usuario.id,
            )
            session.add(nova_conta)
            session.commit()

            # Recarrega a instância da conta para garantir que está associada à sessão e obter o número gerado
            session.refresh(nova_conta)
            return nova_conta

    def excluir_conta(self, cpf: str, numero_conta: int) -> bool:
        usuario_id = self._obter_usuario_id_por_cpf(cpf)

        # Query para encontrar a conta especificada
        query = select(Conta).where(
            Conta.usuario_id == usuario_id, Conta.numero == numero_conta
        )
        conta = self.session.exec(query).first()

        if conta:
            # Verifica se o saldo da conta é zero
            if conta.saldo == 0.0:
                self.session.delete(conta)
                self.session.commit()
                return True
            else:
                return False
        else:
            return False

    def depositar(self, cpf: str, numero_conta: int, valor: float):
        usuario_id = self._obter_usuario_id_por_cpf(cpf)
        query = select(Conta).where(
            Conta.usuario_id == usuario_id, Conta.numero == numero_conta
        )
        conta = self.session.exec(query).first()

        if conta:
            conta.saldo += valor
            self.session.commit()
        else:
            raise ValueError(f"Conta número {numero_conta} não encontrada.")

    def sacar(self, conta_id, valor):
        with self.session as session:
            conta = session.get(Conta, conta_id)
            if valor <= 0:
                raise ValueError("Valor do saque deve ser positivo.")
            if valor > self.limite:
                raise ValueError(
                    f"Não foi possível realizar o saque de R$ {valor:.2f}, pois excede o limite de R$ {self.limite:.2f}. Saldo atual: R$ {conta.saldo:.2f}"
                )
            if valor > conta.saldo:
                raise ValueError("Saldo insuficiente.")
            conta.saldo -= valor
            extrato = Movimentacao(
                conta_id=conta_id, tipo="saque", valor=valor, data=datetime.now()
            )
            session.add(extrato)
            session.commit()
            return f"Saque de R$ {valor:.2f} realizado com sucesso!"

    def obter_saldo_conta(self, cpf: str, numero_conta: int) -> float:
        usuario_id = self._obter_usuario_id_por_cpf(cpf)
        query = select(Conta).where(
            Conta.usuario_id == usuario_id, Conta.numero == numero_conta
        )
        conta = self.session.exec(query).first()
        return conta.saldo if conta else None

    def obter_movimentacoes_conta(self, cpf: str, numero_conta: int):
        usuario_id = self._obter_usuario_id_por_cpf(cpf)
        conta = self.session.exec(
            select(Conta).where(
                Conta.usuario_id == usuario_id, Conta.numero == numero_conta
            )
        ).first()

        if not conta:
            raise ValueError(f"Conta número {numero_conta} não encontrada.")

        # Buscar movimentações associadas à conta
        movimentacoes = self.session.exec(
            select(Movimentacao).where(Movimentacao.conta_id == conta.id)
        ).all()

        return [
            {
                "tipo": "Depósito" if mov.tipo == "deposito" else "Saque",
                "valor": mov.valor,
                "data": mov.data,
            }
            for mov in movimentacoes
        ]

    def _obter_usuario_id_por_cpf(self, cpf: str) -> int:
        query = select(Usuario).where(Usuario.cpf == cpf)
        usuario = self.session.exec(query).first()
        if usuario:
            return usuario.id
        else:
            raise ValueError("Usuário não encontrado com o CPF fornecido.")

    def obter_extrato(self, cpf: str, numero_conta: int):
        with self.session as session:
            usuario_id = self._obter_usuario_id_por_cpf(cpf)

            # Buscar conta
            conta = session.exec(
                select(Conta).where(
                    Conta.usuario_id == usuario_id, Conta.numero == numero_conta
                )
            ).first()

            if not conta:
                raise ValueError(f"Conta número {numero_conta} não encontrada.")

            saldo = conta.saldo

            # Buscar movimentações associadas à conta
            movimentacoes = session.exec(
                select(Movimentacao)
                .where(Movimentacao.conta_id == conta.id)
                .order_by(Movimentacao.data)
            ).all()

            return saldo, movimentacoes
