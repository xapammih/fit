from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import config


metadata_obj = MetaData()
Base = declarative_base(metadata=metadata_obj)

postgres_dsn = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}".format(
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    port=config.POSTGRES_PORT,
    db=config.POSTGRES_DB,
)

engine = create_engine(postgres_dsn)
SessionFactory = sessionmaker(engine, expire_on_commit=False)
