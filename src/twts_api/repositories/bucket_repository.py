from typing import Optional

from sqlalchemy.orm import Session

from twts_api.domain.bucket import Bucket
from .abstract_bucket_repository import AbstractBucketRepository


class BucketRepository(AbstractBucketRepository):

    def __init__(self, session: Session):
        self._session = session

    def add(self, bucket: Bucket):
        self._session.add(bucket)

    def get_by_name(self, name: str = None) -> Optional[Bucket]:
        results = self._session.query(Bucket).filter_by(name=name).all()
        count = len(results)
        assert count <= 1, "More than one bucket with given name - name should be unique!"
        return results.pop() if count == 1 else None

    def get_all(self) -> list[Bucket]:
        return self._session.query(Bucket).all()
