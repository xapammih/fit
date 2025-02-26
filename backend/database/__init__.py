from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

from settings import config


metadata_obj = MetaData()
Base = declarative_base(metadata=metadata_obj)

postgres_dsn = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}".format(
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    port=config.POSTGRES_PORT,
    db=config.POSTGRES_DB,
)

engine = create_async_engine(postgres_dsn)
SessionFactory = async_sessionmaker(engine, expire_on_commit=False)
