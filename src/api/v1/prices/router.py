from fastapi import APIRouter

from api.core.schemas import NotYetImplemented

router = APIRouter(prefix='/prices',
                   tags=['Prices'])


@router.get('', status_code=501)
async def get_prices() -> NotYetImplemented:
    raise NotImplementedError()
