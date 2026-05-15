from fastapi import APIRouter

from . import service, schemas
from api.core.deps.database import DB_SESSION

router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.get('/{user_id}')
async def get_user(user_id: int):
    return [{'station_a': 1.5, 'station_b': 1.6}]


@router.post('/login', status_code=200)
async def login(user: schemas.UserAuth, session: DB_SESSION) -> schemas.User:
    return await service.login(user=user,
                               session=session)


@router.post('/logout')
async def logout():
    return {'message': 'Logout successful'}


@router.post('', status_code=201)
async def create_user(user: schemas.UserAuth, session: DB_SESSION) -> schemas.User:
    return await service.create_user(user=user,
                                     session=session)


@router.delete('/{user_id}')
async def delete_user(user_id: int):
    return {'message': 'User deleted successfully'}


@router.patch('/{user_id}')
async def update_user(user_id: int):
    return {'message': 'User updated successfully'}
