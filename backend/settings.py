import pathlib

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

settings_path = pathlib.Path(__file__).parent.resolve()


class Config(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


config = Config()
