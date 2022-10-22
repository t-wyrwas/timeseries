from abc import ABC, abstractmethod
from typing import Optional

from twts_api.domain.bucket import Bucket


class AbstractBucketRepository(ABC):

    @abstractmethod
    def add(self, bucket: Bucket):
        raise NotImplementedError()

    @abstractmethod
    def get_by_name(self, name: str = None) -> Optional[Bucket]:
        raise NotImplementedError()

    @abstractmethod
    def get_all(self) -> list[Bucket]:
        raise NotImplementedError()
