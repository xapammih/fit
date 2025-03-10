from sqlalchemy import select
from sqlalchemy.orm import Session

from models.users_access.user import UsersModel
from schemas.auth.users import CreateUser
from schemas.auth.users import UpdateUser


class UsersRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, creation_data: CreateUser):
        new_user = UsersModel(
            email=creation_data.email,
            password=creation_data.password,
            first_name=creation_data.first_name,
            last_name=creation_data.last_name,
            phone_number=creation_data.phone_number,
        )
        self.session.add(new_user)
        self.session.flush()
        return new_user

    def update_user(self, user_id: int, update_data: UpdateUser):
        stmt = select(UsersModel).where(UsersModel.id == user_id)
        result = self.session.execute(stmt).scalar()
        if result:
            result.email = update_data.email
            result.first_name = update_data.first_name
            result.last_name = update_data.last_name
            result.phone_number = update_data.phone_number
            self.session.flush()
            return result
        else:
            return None
