from fastapi import APIRouter

router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.get('/{user_id}')
async def get_user(user_id: int):
    return [{'station_a': 1.5, 'station_b': 1.6}]


@router.post('/login')
async def login():
    return {'message': 'Login successful'}


@router.post('/logout')
async def login():
    return {'message': 'Logout successful'}


@router.post('')
async def create_user():
    return {'message': 'Account created'}


@router.delete('/{user_id}')
async def delete_user(user_id: int):
    return {'message': 'User deleted successfully'}


@router.patch('/{user_id}')
async def update_user(user_id: int):
    return {'message': 'User updated successfully'}
