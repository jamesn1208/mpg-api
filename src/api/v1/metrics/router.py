from fastapi import APIRouter

from api.core.schemas import NotYetImplemented

router = APIRouter(prefix='/metrics',
                   tags=['Metrics'])


@router.get('', status_code=501)
async def get_metrics() -> NotYetImplemented:
    raise NotImplementedError()
