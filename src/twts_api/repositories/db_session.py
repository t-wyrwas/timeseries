from sqlalchemy import insert, create_engine, select
from sqlalchemy.orm import Session
from .db_config import DbConfig

def get_session(dbconfig: DbConfig) -> Session:
    engine = create_engine(
        f"{dbconfig.dbtype}://{dbconfig.user}:{dbconfig.password}@{dbconfig.host}:{dbconfig.port}/{dbconfig.dbname}",
        echo=True,
        future=True,
    )
    return Session(engine)
