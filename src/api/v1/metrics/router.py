from fastapi import APIRouter

router = APIRouter(prefix='/metrics',
                   tags=['Metrics'])


@router.get('')
async def get_metrics():
    return [{'station_a': 1.5, 'station_b': 1.6}]

