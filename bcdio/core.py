import json

from datetime import datetime


class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.arquivo_json = "bcdio_data.json"
        self.limite = 500.0
        # Carregar dados do JSON
        try:
            with open(self.arquivo_json, "r") as f:
                dados = json.load(f)
                self.saldo = dados["saldo"]
                self.extrato = dados["extrato"]
        except FileNotFoundError:
            pass

    # Calcula o saldo após atualizar o extrato
    def salvar_dados(self):
        dados = {"saldo": self.saldo, "extrato": self.extrato}
        try:
            with open(self.arquivo_json, "w") as f:
                json.dump(dados, f, indent=2)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def calcular_saldo(self, extrato):
        saldo = 0
        for transacao in extrato:
            if transacao["tipo"] == "depósito":
                saldo += transacao["valor"]
            else:
                saldo -= transacao["valor"]
        return saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(
                {
                    "tipo": "depósito",
                    "valor": valor,  # Update the value here
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
            self.salvar_dados()  # Pass the value here
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do saque deve ser positivo.")
        if valor > self.limite:
            raise ValueError("Valor do saque excede o limite.")
        self.saldo -= valor
        self.extrato.append(
            {
                "tipo": "saque",
                "valor": valor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        self.salvar_dados()
        return f"Saque de R$ {valor:.2f} realizado com sucesso!"

    def mostrar_extrato(self):
        extrato_text = "\n================= EXTRATO =================\n"
        for operacao in self.extrato:
            data_formatada = datetime.strptime(
                operacao["data"], "%Y-%m-%d %H:%M:%S"
            ).strftime("%d/%m/%Y %H:%M:%S")
            extrato_text += (
                f"{operacao['tipo']}: R$ {operacao['valor']:.2f} - {data_formatada}\n"
            )
        extrato_text += f"\nSaldo: R$ {self.saldo:.2f}\n"
        extrato_text += "============================================"
        return extrato_text
