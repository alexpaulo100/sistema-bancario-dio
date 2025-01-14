from sqlmodel import create_engine, Session, select
from bcdio.models import Movimentacao, Usuario


# Ajuste o caminho para o banco de dados conforme necessário
DATABASE_URL = "sqlite:////home/alextech/projetos/projeto-link/sistema-bancario-dio/assets/bcdio.db"

# Criação do engine com SQLModel
engine = create_engine(DATABASE_URL, echo=True)


# Função para obter a sessão
def get_session():
    return Session(engine)


def add_usuarios(session: Session, instance: Usuario):
    """Salvar usuários no banco de dados.
    - Se o usuário já existir, atualiza. Se não, cria um novo.
    """
    existing = session.exec(
        select(Usuario).where(Usuario.cpf == instance.cpf)
    ).first()

    created = existing is None
    if created:
        session.add(instance)
        set_initial_contas(session, instance)
    else:
        existing.contas = instance.contas
        session.add(existing)
        session.refresh(existing)

    session.commit()
    return instance, created


def set_initial_contas(session: Session, usuario: Usuario):
    """Define a movimentação inicial para um usuário ao criar a conta."""
    saldo = 0.0
    add_movimentacao(session, usuario, saldo)


def add_movimentacao(
    session: Session,
    usuario: Usuario,
    saldo: float,
):
    """Adiciona uma movimentação para um usuário com o saldo inicial
    ou atualizado."""
    movimentacao = Movimentacao(usuario=usuario, saldo=saldo)
    session.add(movimentacao)
    session.commit()

    movimentacoes = session.exec(
        select(Movimentacao).where(Movimentacao.usuario == usuario)
    ).all()

    total = sum(mov.saldo for mov in movimentacoes)

    existing_moviment = session.exec(
        select(Movimentacao)
        .where(Movimentacao.usuario == usuario)
        .order_by(Movimentacao.id.desc())
    ).first()

    if existing_moviment:
        existing_moviment.saldo = total
        session.add(existing_moviment)
    else:
        # Garantir que estamos adicionando a movimentação final
        session.add(Movimentacao(usuario=usuario, saldo=total))

    session.commit()
