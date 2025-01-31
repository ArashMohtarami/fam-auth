import os
from pydantic_settings import BaseSettings
from decouple import config

# Retrieve database configuration settings from environment variables or config files
DB_USER = config.get("DB_USER")
DB_PASSWORD = config.get("DB_PASSWORD")
DB_NAME = config.get("DB_NAME")
DB_HOST = config.get("DB_HOST")


class Settings(BaseSettings):
    """
    Settings class for configuration management.

    This class is used to retrieve and manage database configuration settings for
    the application. It inherits from `BaseSettings` provided by Pydantic, which allows
    for easy management of environment variables and settings.

    Attributes:
        DATABASE_URL (str): The URL used to connect to the PostgreSQL database for synchronous operations.
        ASYNC_DATABASE_URL (str): The URL used to connect to the PostgreSQL database for asynchronous operations.
    """

    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    """
    The URL used to connect to the PostgreSQL database for synchronous operations.

    This URL is formed using the following format:
        postgresql://{user}:{password}@{host}/{dbname}
    
    The values for `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_NAME` are retrieved from 
    environment variables or configuration files.

    Attributes:
        str: Database connection URL for synchronous operations.
    """

    ASYNC_DATABASE_URL: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    """
    The URL used to connect to the PostgreSQL database for asynchronous operations.

    This URL is similar to `DATABASE_URL`, but it includes the `asyncpg` driver for async support.

    Attributes:
        str: Database connection URL for asynchronous operations.
    """


# Instantiate settings object to be used in the application
settings = Settings()
