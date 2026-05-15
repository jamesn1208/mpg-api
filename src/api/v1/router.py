from fastapi import APIRouter

from api.v1.prices.router import router as prices_router

v1_router = APIRouter(prefix='/v1')
v1_router.include_router(prices_router)

