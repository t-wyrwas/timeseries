from typing import Optional

from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from domain.bucket import Bucket
from repositories import DbConfig, get_session


class BucketRepository:

    def __init__(self, dbconfig: Optional[DbConfig] = None):
        self._dbconfig = dbconfig if dbconfig != None else DbConfig.from_env()

    def add(self, bucket: Bucket):
        with get_session(self._dbconfig) as session:
            session.execute(insert(Bucket), [{"name": bucket.name}])

    def get(self, name: str) -> Optional[Bucket]:
        with get_session(self._dbconfig) as session:
            stmt = select(Bucket).filter_by(name=name)
            result = session.execute(stmt)
            buckets = result.scalars.all()
            bucket_count = len(buckets)
            assert bucket_count <= 1, "More than one bucket with given name - name should be unique!"
            return buckets[0] if bucket_count > 0 else None
