from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.user import User
from src.schemas.user import UserCreateSchema


class UserQuery:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_id(self, user_id: int):
        result = await self.db.execute(select(User).filter(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_all_users(self):
        result = await self.db.execute(select(User))
        return result.scalars().all()

    async def create_user(self, user_data: UserCreateSchema):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user
