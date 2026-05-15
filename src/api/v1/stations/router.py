from fastapi import APIRouter

router = APIRouter(prefix='/stations',
                   tags=['Stations'])


@router.get('')
async def get_stations():
    return [{'station_a': 1.5, 'station_b': 1.6}]
