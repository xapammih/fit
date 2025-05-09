from sqlalchemy.orm import Session

from repositories.users import UsersRepository


class UnitOfWork:
    def __init__(self, session: Session):
        self._session = session

        self.users = UsersRepository(session)

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()


class UnitOfWorkManager:
    def __init__(self, unit_of_work: UnitOfWork):
        self._unit_of_work = unit_of_work

    def __enter__(self) -> UnitOfWork:
        return self._unit_of_work

    def __exit__(self, type, value, traceback):
        if type is None:
            self._unit_of_work.commit()
        else:
            self._unit_of_work.rollback()
