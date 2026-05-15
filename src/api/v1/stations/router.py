from fastapi import APIRouter

from api.core.schemas import NotYetImplemented

router = APIRouter(prefix='/stations',
                   tags=['Stations'])


@router.get('/{station_id}', status_code=501)
async def get_station(station_id: int) -> NotYetImplemented:
    raise NotImplementedError()
