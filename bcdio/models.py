from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"  # Nome da tabela ajustado

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    cpf: str = Field(unique=True)
    data_nascimento: str
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str

    # Relacionamento com Conta
    contas: List["Conta"] = Relationship(back_populates="usuario")

    # Relacionamento com Movimentacao
    movimentacoes: List["Movimentacao"] = Relationship(back_populates="usuario")


class Conta(SQLModel, table=True):
    __tablename__ = "conta"  # Nome da tabela ajustado

    id: Optional[int] = Field(default=None, primary_key=True)
    numero: int
    agencia: str
    saldo: float

    # Chave estrangeira para Usuario
    usuario_id: int = Field(
        foreign_key="usuario.id"
    )  # Atualizado para refletir o nome da tabela

    # Relacionamento com Usuario
    usuario: Usuario = Relationship(back_populates="contas")

    # Relacionamento com Movimentacao
    movimentacoes: List["Movimentacao"] = Relationship(back_populates="conta")


class Movimentacao(SQLModel, table=True):
    __tablename__ = "movimentacao"

    id: Optional[int] = Field(default=None, primary_key=True)
    tipo: str = Field(nullable=False)  # Tipo da movimentação
    valor: float = Field(nullable=False)
    data: datetime = Field(default=datetime.utcnow)  # Alterado para datetime

    conta_id: int = Field(foreign_key="conta.id")
    conta: "Conta" = Relationship(back_populates="movimentacoes")

    usuario_id: int = Field(foreign_key="usuario.id")
    usuario: "Usuario" = Relationship(back_populates="movimentacoes")
