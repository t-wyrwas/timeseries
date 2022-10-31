from fastapi.routing import APIRouter
from .metadata import router as metadata_router

routes = APIRouter()
routes.include_router(metadata_router)
