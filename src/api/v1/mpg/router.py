from fastapi import APIRouter

from api.core.deps.database import DB_SESSION
from api.core.deps.auth import USER_ID
from api.core.schemas import ActionResponse
from . import schemas, service

router = APIRouter(prefix='/mpg',
                   tags=['MPG'])


@router.get('')
async def get_mpg_history(session: DB_SESSION,
                          user_id: USER_ID,
                          limit: int = 10,
                          offset: int = 0) -> list[schemas.MPGLog]:
    return await service.get_mpg_history(limit=limit,
                                         offset=offset,
                                         session=session,
                                         user_id=user_id)


@router.post('')
async def log_mpg(log: schemas.MPGLog,
                  session: DB_SESSION,
                  user_id: USER_ID) -> ActionResponse:
    return await service.log_mpg(log=log,
                                 session=session,
                                 user_id=user_id)
