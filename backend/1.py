from sqlalchemy import create_engine

postgres_dsn = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}".format(
    user="postgres",
    password="123",
    host="localhost",
    port=5432,
    db="fit",
)
engine = create_engine(postgres_dsn)
connection = engine.connect()
