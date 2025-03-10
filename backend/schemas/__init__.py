from pydantic import BaseModel
from pydantic import ConfigDict


class ConfBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
