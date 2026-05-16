from fastapi import APIRouter

from . import schemas
from api.core.schemas import ActionResponse
from api.core.deps.auth import USER_ID
from api.core.deps.database import DB_SESSION

router = APIRouter(prefix='/vehicles',
                   tags=['Vehicles'])


@router.get('', status_code=200)
async def get_vehicles(session: DB_SESSION,
                       user_id: USER_ID,
                       limit: int = 10,
                       offset: int = 0) -> list[schemas.Vehicle]:
    # List all vehicles that a user has linked to them, with pagination
    return {}


@router.get('', status_code=200)
async def check_vehicle(session: DB_SESSION,
                        user_id: USER_ID,
                        vehicle: schemas.CheckVehicle) -> ActionResponse:
    # Get details from Gov.UK API & return to front end where the user can edit them
    return {}


@router.post('', status_code=201)
async def add_vehicle(session: DB_SESSION,
                      user_id: USER_ID,
                      vehicle: schemas.AddVehicle) -> ActionResponse:
    # Add vehicle with (potentially) updated information from front end
    return {}
