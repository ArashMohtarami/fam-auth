from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.data_access.querysets.user import UserQuery


class UserManager:
    def __init__(self, db: AsyncSession):
        self.db = db

    def get_query(self):
        return UserQuery(self.db)

    async def get_user_by_id(self, user_id):
        return await self.get_query().get_user_by_id(user_id=user_id)

    async def get_all_users(self):
        return await self.get_query().get_all_users()

    async def create_user(self, user_data: dict):
        return await self.get_query().create_user(user_data=user_data)
