from fastapi.routing import APIRouter

router = APIRouter(prefix='/metadata')

@router.get('/buckets')
def list_buckets():
    return ['bucket1', 'bucket2']
