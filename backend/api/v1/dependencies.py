from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.orm import Session

from database.session import get_session
from database.unit_of_work import UnitOfWork
from database.unit_of_work import UnitOfWorkManager


def get_unit_of_work(session: Annotated[Session, Depends(get_session)]):
    return UnitOfWork(session)


def get_unit_of_work_manager(
    unit_of_work: Annotated[UnitOfWork, Depends(get_unit_of_work)]
):
    return UnitOfWorkManager(unit_of_work)


UnitOfWorkDep = Annotated[UnitOfWork, Depends(get_unit_of_work)]
UnitOfWorkManagerDep = Annotated[UnitOfWorkManager, Depends(get_unit_of_work_manager)]
