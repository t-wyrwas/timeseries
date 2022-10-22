from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from twts_api.domain.bucket import Bucket
from twts_api.repositories import DbConfig, get_session


class BucketRepository:

    def __init__(self, dbconfig: Optional[DbConfig] = None):
        self._dbconfig = dbconfig if dbconfig != None else DbConfig.from_env()

    def add(self, bucket: Bucket):
        with get_session(self._dbconfig) as session:
            session.add(bucket)
            session.commit()

    def get_by_name(self, name: str = None) -> Optional[Bucket]:
        with get_session(self._dbconfig) as session:
            results = session.query(Bucket).filter_by(name=name).all()
            count = len(results)
            assert count <= 1, "More than one bucket with given name - name should be unique!"
            return results.pop() if count == 1 else None

    def get_all(self) -> list[Bucket]:
        with get_session(self._dbconfig) as session:
            return session.query(Bucket).all()
