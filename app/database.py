from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

# from app.config import get_db_url

DATABASE_URL = "postgresql+asyncpg://test_user:test_pas@db/test_db"
# DATABASE_URL = get_db_url()
# print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase): pass
