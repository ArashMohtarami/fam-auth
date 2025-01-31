from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.repository.data_access.manager.user import UserManager
from src.core.database import AsyncSessionLocal


async def get_db():
    """
    Dependency that provides a database session for interacting with the database.

    This function uses the `AsyncSessionLocal` context manager to create an asynchronous 
    database session that is automatically closed after the request is finished.

    Yields:
        AsyncSession: The database session to interact with the database.
    
    Example:
        db = await get_db()
        # Use db to perform database operations.
    """
    async with AsyncSessionLocal() as db:
        yield db


async def get_user_manager(db: AsyncSession = Depends(get_db)):
    """
    Dependency that provides a user manager for interacting with user-related data.

    This function receives a database session (`db`) and returns a `UserManager` instance 
    which can be used to perform user-related operations like creating, reading, updating, 
    or deleting users.

    Args:
        db (AsyncSession): The database session to use for the `UserManager` instance. 
                            Defaults to the session provided by `get_db`.

    Returns:
        UserManager: An instance of the `UserManager` class that provides user-related methods.

    Example:
        user_manager = await get_user_manager(db)
        # Use user_manager to interact with user data.
    """
    return UserManager(db)
