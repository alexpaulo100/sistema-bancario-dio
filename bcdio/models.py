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
    __tablename__ = "movimentacao"  # Nome da tabela ajustado

    id: Optional[int] = Field(default=None, primary_key=True)
    tipo: str
    valor: float
    data: str

    # Chave estrangeira para Conta
    conta_id: int = Field(
        foreign_key="conta.id"
    )  # Atualizado para refletir o nome da tabela

    # Relacionamento com Conta
    conta: Conta = Relationship(back_populates="movimentacoes")

    # Chave estrangeira para Usuario
    usuario_id: int = Field(
        foreign_key="usuario.id"
    )  # Atualizado para refletir o nome da tabela
    usuario: Usuario = Relationship(back_populates="movimentacoes")
