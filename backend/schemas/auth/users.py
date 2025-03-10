from schemas import ConfBaseModel


class CreateUser(ConfBaseModel):
    first_name: str
    last_name: str
    email: str
    password_hash: str
    phone_number: str


class UpdateUser(ConfBaseModel):
    first_name: str
    last_name: str
    email: str
    password_hash: str


class UserResponse(ConfBaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
