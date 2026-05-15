from fastapi import APIRouter

router = APIRouter(prefix='/mpg',
                   tags=['MPG'])


@router.get('')
async def get_mpg_history(limit: int = 10, offset: int = 0):
    return [{'station_a': 1.5, 'station_b': 1.6}]


@router.post('')
async def log_mpg():
    return {'message': 'Log received'}
