from fastapi import APIRouter

from api.v1.calories_calc import router as calories_calc_router
from api.v1.routers import router as healthcheck_router
from api.v1.users.users import router as users_router


router = APIRouter(prefix="/v1")

router.include_router(healthcheck_router, prefix="/healthcheck", tags=["Healthcheck"])
router.include_router(
    calories_calc_router, prefix="/calories_calc", tags=["Calories_calc"]
)
router.include_router(users_router, prefix="/users", tags=["Users"])

__all__ = ["router"]
