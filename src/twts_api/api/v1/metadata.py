from fastapi import status
from fastapi.routing import APIRouter
from fastapi.responses import PlainTextResponse

from twts_api.domain.bucket import Bucket, Timeserie
from twts_api.repositories import DbConfig
from twts_api.services import SqlAlchemyUnitOfWork

import twts_api.api.v1.dtos as dtos

router = APIRouter(prefix="/metadata")


@router.get("/buckets", status_code=status.HTTP_200_OK)
def list_buckets() -> list[dtos.Bucket]:
    uow = SqlAlchemyUnitOfWork(db_config=DbConfig.from_env())
    with uow:
        repo = uow.get_bucket_repository()
        bucket_dtos = []
        for bucket in repo.get_all():
            timeseries = bucket.get_all();
            bucket_dtos.append(dtos.Bucket(name=bucket.name, timeseries=[dtos.Timeserie(name=t.name) for t in timeseries]))
    return bucket_dtos

@router.post("/buckets", status_code=status.HTTP_201_CREATED)
def add_bucket(name: str):
    uow = SqlAlchemyUnitOfWork(db_config=DbConfig.from_env())
    with uow:
        repo = uow.get_bucket_repository()
        repo.add(Bucket(name=name))
        uow.commit()

@router.post("/buckets/{bucket_name}", status_code=status.HTTP_201_CREATED)
def add_timeserie(bucket_name: str, timeserie: dtos.Timeserie):
    uow = SqlAlchemyUnitOfWork(db_config=DbConfig.from_env())
    with uow:
        bucket_repo = uow.get_bucket_repository()
        bucket = bucket_repo.get_by_name(bucket_name)
        if bucket is None:
            return PlainTextResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Bucket does not exist")
        bucket.add(Timeserie(name=timeserie.name))
        uow.commit()
