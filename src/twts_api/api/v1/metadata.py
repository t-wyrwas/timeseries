from fastapi.routing import APIRouter

from twts_api.domain.bucket import Bucket
from twts_api.repositories import BucketRepository

router = APIRouter(prefix="/metadata")


@router.get("/buckets")
def list_buckets() -> list[Bucket]:
    repo = BucketRepository()
    return repo.get_all()

@router.post("/buckets")
def add_bucket(name: str):
    repo = BucketRepository()
    repo.add(Bucket(name=name))
