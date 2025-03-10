from fastapi import APIRouter

from api.v1.dependencies import UnitOfWorkManagerDep

router = APIRouter()


@router.get("/create")
def create_user(uow_manager: UnitOfWorkManagerDep):
    ...
