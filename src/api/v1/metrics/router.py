from fastapi import APIRouter
import logging

from api.core.deps.database import DB_SESSION
from . import service

router = APIRouter(prefix='/metrics',
                   tags=['Metrics'])


@router.get('')
async def get_metrics(session: DB_SESSION):
    return await service.get_metrics(session)
