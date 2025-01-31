from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.core.settings import settings
from contextlib import asynccontextmanager

# Define the asynchronous database URL from the settings
SQLALCHEMY_DATABASE_URL = settings.ASYNC_DATABASE_URL
"""
Database URL for SQLAlchemy.

This variable stores the database connection URL used to connect to the database asynchronously.
The URL is fetched from the application settings and used to create an asynchronous SQLAlchemy engine.

Attributes:
    SQLALCHEMY_DATABASE_URL (str): The URL for the PostgreSQL database connection used by SQLAlchemy.
"""

# Create an asynchronous SQLAlchemy engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
"""
Asynchronous SQLAlchemy engine.

This engine is responsible for managing asynchronous interactions with the PostgreSQL database.
The `echo=True` option ensures that SQL statements are logged during execution.

Attributes:
    engine (AsyncEngine): The asynchronous SQLAlchemy engine used to communicate with the database.
"""

# Create an asynchronous session factory
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
"""
Asynchronous session factory.

This factory is used to create new session instances that allow interaction with the database.
The `expire_on_commit=False` option ensures that session objects do not expire after commit.

Attributes:
    AsyncSessionLocal (sessionmaker): The asynchronous session factory used to create session objects.
"""

# Define the base class for SQLAlchemy models
Base = declarative_base()
"""
Base class for SQLAlchemy models.

This base class is used to define database models. All models should inherit from this class to work with SQLAlchemy ORM.

Attributes:
    Base (DeclarativeMeta): The base class used to define SQLAlchemy models.
"""

@asynccontextmanager
async def get_db():
    """
    Asynchronous database session manager.

    This context manager is responsible for creating and yielding an asynchronous database session.
    It ensures that the session is committed after the operations are completed.

    Yields:
        AsyncSession: An asynchronous session that can be used to interact with the database.
    
    Example usage:
        ```python
        async with get_db() as db:
            # perform database operations
        ```

    Attributes:
        session (AsyncSession): The asynchronous session used to interact with the database.
    """
    async with AsyncSessionLocal() as session:
        yield session
        await session.commit()
