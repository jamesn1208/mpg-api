from fastapi import APIRouter

from api.v1.prices.router import router as prices_router
from api.v1.stations.router import router as stations_router
from api.v1.metrics.router import router as metrics_router


v1_router = APIRouter(prefix='/v1')
v1_router.include_router(prices_router)
v1_router.include_router(stations_router)
v1_router.include_router(metrics_router)
