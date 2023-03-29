from fastapi import APIRouter

from .statistic import statistic

api_router = APIRouter(prefix="/api")

api_router.include_router(statistic.router, prefix="/statistic", tags=["statistic"])
