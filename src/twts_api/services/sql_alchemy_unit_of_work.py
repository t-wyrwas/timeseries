from sqlalchemy.orm import Session

from twts_api.repositories import get_session, DbConfig
from twts_api.repositories.bucket_repository import BucketRepository
from .abstract_unit_of_work import AbstractUnitOfWork


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self, db_config: DbConfig, session_factory = get_session):
        self._session_factory = session_factory
        self._db_config = db_config
        self._session: Session = None

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()

    def get_bucket_repository(self) -> BucketRepository:
        return BucketRepository(self._session)

    def __enter__(self):
        self._session = self._session_factory(self._db_config)

    def __exit__(self, *args):
        super().__exit__(*args)
        self._session.close()
