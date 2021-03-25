import os
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import settings

# выбор конфига для подключения БД в зависимости от окружения
configuration = os.environ.get("CONFIG")
if configuration == "HEROKU":
    # подключение к Heroku Postgres
    url = os.environ.get("DATABASE_URL")
else:
    # подключение на тестовом сервере
    url = URL.create(
        drivername="postgresql",
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        host='localhost',
        port=5432,
        database=settings.DB_NAME
    )

engine = create_engine(url,echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)