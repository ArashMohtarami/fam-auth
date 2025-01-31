from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.user import User
from src.schemas.user import UserCreateSchema


class UserQuery:
    """
    A class to interact with the user-related database queries.

    This class provides methods to query, create, and manipulate user data 
    within the database using SQLAlchemy ORM and async session handling.

    Attributes:
        db (AsyncSession): The SQLAlchemy asynchronous session used for executing queries.
    """

    def __init__(self, db: AsyncSession):
        """
        Initializes the UserQuery class with the database session.

        Args:
            db (AsyncSession): The SQLAlchemy asynchronous session.
        """
        self.db = db

    async def get_user_by_id(self, user_id: int):
        """
        Get a user by their unique ID.

        This method retrieves a user from the database using their unique ID.

        Args:
            user_id (int): The unique ID of the user to retrieve.

        Returns:
            User or None: The user object if found, otherwise None.
        """
        result = await self.db.execute(select(User).filter(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_all_users(self):
        """
        Get all users from the database.

        This method retrieves all users in the database.

        Returns:
            list[User]: A list of all user objects.
        """
        result = await self.db.execute(select(User))
        return result.scalars().all()

    async def create_user(self, user_data: UserCreateSchema):
        """
        Create a new user in the database.

        This method takes in user data, creates a new user record in the database, 
        and commits the transaction.

        Args:
            user_data (UserCreateSchema): The data required to create a new user.

        Returns:
            User: The newly created user object.
        """
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user
