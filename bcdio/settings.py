import os

ROOT_PATH: str = os.path.dirname(__file__)
DATABASE_PATH: str = os.path.join(ROOT_PATH, "..", "assets", "bcdio.db")
SQL_CON_STRING = f"sqlite:///{DATABASE_PATH}"
