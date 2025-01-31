from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.repository.data_access.manager.user import UserManager
from src.core.database import AsyncSessionLocal


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


async def get_user_manager(db: AsyncSession = Depends(get_db)):
    return UserManager(db)
