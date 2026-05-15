from fastapi import APIRouter

from api.v1.prices.router import router as prices_router
from api.v1.stations.router import router as stations_router
from api.v1.metrics.router import router as metrics_router
from api.v1.users.router import router as users_router
from api.v1.mpg.router import router as mpg_router


v1_router = APIRouter(prefix='/v1')
v1_router.include_router(prices_router)
v1_router.include_router(stations_router)
v1_router.include_router(metrics_router)
v1_router.include_router(users_router)
v1_router.include_router(mpg_router)
