from fastapi.routing import APIRouter

from twts_api.domain.bucket import Bucket
from twts_api.repositories import BucketRepository, DbConfig
from twts_api.services import SqlAlchemyUnitOfWork

import twts_api.api.v1.dto as dto

router = APIRouter(prefix="/metadata")


@router.get("/buckets")
def list_buckets() -> list[dto.Bucket]:
    uow = SqlAlchemyUnitOfWork(db_config=DbConfig.from_env())
    with uow:
        repo = uow.get_bucket_repository()
        bucketDtos = [dto.Bucket(name=i.name) for i in repo.get_all()]
    return bucketDtos

@router.post("/buckets")
def add_bucket(name: str):
    uow = SqlAlchemyUnitOfWork(db_config=DbConfig.from_env())
    with uow:
        repo = uow.get_bucket_repository()
        repo.add(Bucket(name=name))
        uow.commit()
