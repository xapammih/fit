from dataclasses import dataclass

from database.unit_of_work import UnitOfWorkManager
from schemas.auth.users import CreateUser
from schemas.auth.users import UserResponse


@dataclass
class CreateUserUseCase:
    uow_manager: UnitOfWorkManager
    creation_data: CreateUser

    def __call__(self):
        with self.uow_manager as uow:
            new_user = uow.users.create_user(self.creation_data)
            new_user = UserResponse.model_validate(new_user)
            return new_user
