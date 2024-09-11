from sqlmodel import Session, create_engine

from bcdio import models
from bcdio.settings import SQL_CON_STRING

# Cria o engine
engine = create_engine(SQL_CON_STRING, echo=False)

# Cria as tabelas no banco de dados
models.SQLModel.metadata.create_all(bind=engine)


def get_session() -> Session:
    """Retorna uma nova sessão do banco de dados."""
    return Session(bind=engine)
