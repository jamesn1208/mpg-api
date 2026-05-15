from fastapi import APIRouter, Response

from . import service, schemas
from api.core.deps.database import DB_SESSION
from api.core.deps.auth import USER_ID
from api.core.schemas import ActionResponse

router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.post('/login', status_code=200)
async def login(user: schemas.UserAuth, session: DB_SESSION, response: Response) -> schemas.User:
    data = await service.login(user=user,
                               session=session)
    # Set auth cookie
    response.set_cookie(key='X-Auth-Token',
                        value=data.token,
                        httponly=True,
                        samesite='strict',
                        expires=2628000)  # 1 month
    return data


@router.post('/logout')
async def logout(user_id: USER_ID, session: DB_SESSION, response: Response) -> ActionResponse:
    # Clear auth cookie
    response.set_cookie(key='X-Auth-Token',
                        value="",
                        httponly=True,
                        samesite='strict',
                        expires=2628000)  # 1 month
    return await service.logout(user_id=user_id,
                                session=session)


@router.post('', status_code=201)
async def create_user(user: schemas.UserAuth, session: DB_SESSION, response: Response) -> schemas.User:
    data = await service.create_user(user=user,
                                     session=session)
    # Set auth cookie
    response.set_cookie(key='X-Auth-Token',
                        value=data.token,
                        httponly=True,
                        samesite='strict',
                        expires=2628000)  # 1 month
    return data


@router.delete('/{user_id}')
async def delete_user(user_id: int, session: DB_SESSION, _: USER_ID, response: Response) -> ActionResponse:
    # Clear auth cookie
    response.set_cookie(key='X-Auth-Token',
                        value="",
                        httponly=True,
                        samesite='strict',
                        expires=2628000)  # 1 month
    return await service.delete_user(user_id=user_id,
                                     session=session)


@router.patch('/{user_id}')
async def update_user(user_id: int, user: schemas.UserUpdate, session: DB_SESSION, _: USER_ID) -> ActionResponse:
    return await service.update_user(user_id=user_id,
                                     user=user,
                                     session=session)
