from fastapi import APIRouter

from . import schemas
from api.core.schemas import ActionResponse

router = APIRouter(prefix='/vehicles',
                   tags=['Vehicles'])


@router.get('', status_code=200)
async def get_vehicles(limit: int = 10, offset: int = 0) -> list[schemas.Vehicle]:
    return {}


@router.post('', status_code=200)
async def add_vehicle(vehicle: schemas.AddVehicle) -> ActionResponse:
    return {}
