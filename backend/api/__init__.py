from fastapi import APIRouter

from api.v1.calories_calc import router as calories_calc_router
from api.v1.routers import router as healthcheck_router


router = APIRouter(prefix="/v1")

router.include_router(healthcheck_router, prefix="/healthcheck", tags=["healthcheck"])
router.include_router(
    calories_calc_router, prefix="/calories_calc", tags=["calories_calc"]
)

__all__ = ["router"]
