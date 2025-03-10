from schemas import ConfBaseModel


class CreateUser(ConfBaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password_hash: str
