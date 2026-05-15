from fastapi import APIRouter

router = APIRouter(prefix='/prices',
                   tags=['Prices'])


@router.get('/')
async def get_prices():
    return [{'station_a': 1.5, 'station_b': 1.6}]
