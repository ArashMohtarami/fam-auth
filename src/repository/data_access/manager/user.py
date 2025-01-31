from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.data_access.querysets.user import UserQuery


class UserManager:
    """
    A class to manage user-related operations in the database.

    This class provides methods to query, create, and manipulate user data 
    within the database by interacting with the `UserQuery` class.

    Attributes:
        db (AsyncSession): The SQLAlchemy asynchronous session used for executing queries.
    """

    def __init__(self, db: AsyncSession):
        """
        Initializes the UserManager class with the database session.

        Args:
            db (AsyncSession): The SQLAlchemy asynchronous session.
        """
        self.db = db

    def get_query(self):
        """
        Get an instance of the `UserQuery` class for querying user data.

        Returns:
            UserQuery: An instance of `UserQuery` to interact with the user database.
        """
        return UserQuery(self.db)

    async def get_user_by_id(self, user_id):
        """
        Get a user by their unique ID.

        This method retrieves a user from the database using their unique ID.

        Args:
            user_id: The unique ID of the user to retrieve.

        Returns:
            User or None: The user object if found, otherwise None.
        """
        return await self.get_query().get_user_by_id(user_id=user_id)

    async def get_all_users(self):
        """
        Get all users from the database.

        This method retrieves all users from the database.

        Returns:
            list[User]: A list of all user objects.
        """
        return await self.get_query().get_all_users()

    async def create_user(self, user_data: dict):
        """
        Create a new user in the database.

        This method takes in user data, creates a new user record in the database, 
        and commits the transaction.

        Args:
            user_data (dict): A dictionary containing the data required to create a new user.

        Returns:
            User: The newly created user object.
        """
        return await self.get_query().create_user(user_data=user_data)
