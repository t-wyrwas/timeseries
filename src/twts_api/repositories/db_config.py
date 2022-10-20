from dataclasses import dataclass
import os

@dataclass
class DbConfig:
    host: str = "localhost"
    port: str = "5432"
    dbname: str = "twts"
    user: str = "postgres"
    password: str = "postgres"
    dbtype: str = "postgresql+psycopg2"

    @classmethod
    def from_env(cls) -> "DbConfig":
        cls_name = cls.__name__.lower()
        host = os.environ.get(f"{cls_name}_host", cls.host)
        port = os.environ.get(f"{cls_name}_port", cls.port)
        dbname = os.environ.get(f"{cls_name}_dbname", cls.dbname)
        user = os.environ.get(f"{cls_name}_user", cls.user)
        password = os.environ.get(f"{cls_name}_password", cls.password)
        dbtype = os.environ.get(f"{cls_name}_dbtype", cls.dbtype)
        return DbConfig(host=host, port=port, dbname=dbname, user=user, password=password, dbtype=dbtype)
