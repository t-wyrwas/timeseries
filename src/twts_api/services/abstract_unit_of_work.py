from abc import ABC, abstractmethod

from twts_api.repositories import AbstractBucketRepository

class AbstractUnitOfWork(ABC):

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()

    @abstractmethod
    def get_bucket_repository() -> AbstractBucketRepository:
        raise NotImplementedError()

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError()

    @abstractmethod
    def __exit__(self, *args):
        self.rollback()
