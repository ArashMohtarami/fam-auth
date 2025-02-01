from pydantic import BaseModel, EmailStr, Field, UUID4
from datetime import datetime, date
from typing import Optional


class UserBaseSchema(BaseModel):
    """
    Base schema for user data.

    This schema includes common fields for a user, such as `username`, `email`, 
    `first_name`, `last_name`, `phone_number`, and `birth_date`.

    Attributes:
        username (str): Unique username for the user, with a minimum length of 4 characters.
        email (EmailStr): Valid email address of the user.
        first_name (Optional[str]): First name of the user (optional, max length 100 characters).
        last_name (Optional[str]): Last name of the user (optional, max length 100 characters).
        phone_number (Optional[str]): Phone number of the user (optional).
        birth_date (Optional[datetime]): Birthdate of the user (optional).
    """
    username: str = Field(
        ...,
        min_length=4,
        description="Unique username with at least 4 characters."
    )
    email: EmailStr = Field(
        ...,
        description="Valid email address."
    )
    first_name: Optional[str] = Field(
        None,
        max_length=100,
        description="First name of the user."
    )
    last_name: Optional[str] = Field(
        None,
        max_length=100,
        description="Last name of the user."
    )
    phone_number: Optional[str] = Field(
        None,
        description="Phone number of the user."
    )
    birth_date: Optional[datetime] = Field(
        None,
        description="Birthdate of the user."
    )


class UserCreateSchema(UserBaseSchema):
    """
    Schema for creating a user.

    Inherits from `UserBaseSchema` and includes a `password` field.

    Attributes:
        password (str): Password for the user.
    """
    password: str = Field(
        ...,
        description="Password for the user."
    )
    confirm_password: str = Field(
        ...,
        description="Confirm password for the user."
    )


class UserUpdateSchema(UserBaseSchema):
    """
    Schema for updating an existing user.

    Inherits from `UserBaseSchema` and includes optional fields like `password` and `is_active`.

    Attributes:
        password (Optional[str]): Password for the user (optional).
        is_active (Optional[bool]): Flag indicating if the user is active (optional).
    """
    password: Optional[str] = Field(
        None,
        description="Password for the user."
    )
    is_active: Optional[bool] = Field(
        None,
        description="Flag indicating if the user is active."
    )


class UserPatchSchema(BaseModel):
    """
    Schema for patching user data.

    This schema allows for partial updates of user data, including fields like `username`, 
    `email`, `first_name`, `last_name`, `phone_number`, `birth_date`, `image`, `password`, 
    and `is_active`.

    Attributes:
        username (Optional[str]): Unique username with at least 4 characters (optional).
        email (Optional[EmailStr]): Valid email address (optional).
        first_name (Optional[str]): First name of the user (optional).
        last_name (Optional[str]): Last name of the user (optional).
        phone_number (Optional[str]): Phone number of the user (optional).
        birth_date (Optional[date]): Birthdate of the user (optional).
        image (Optional[str]): URL or path to the user's profile image (optional).
        password (Optional[str]): Password for the user (optional).
        is_active (Optional[bool]): Flag indicating if the user is active (optional).
    """
    username: Optional[str] = Field(
        None, min_length=4,
        description="Unique username with at least 4 characters."
    )
    email: Optional[EmailStr] = Field(
        None,
        description="Valid email address."
    )
    first_name: Optional[str] = Field(
        None, max_length=100,
        description="First name of the user."
    )
    last_name: Optional[str] = Field(
        None, max_length=100,
        description="Last name of the user."
    )
    phone_number: Optional[str] = Field(
        None,
        description="Phone number of the user."
    )
    birth_date: Optional[date] = Field(
        None,
        description="Birthdate of the user."
    )
    image: Optional[str] = Field(
        None,
        description="URL or path to the user's profile image."
    )
    password: Optional[str] = Field(
        None,
        description="Password for the user."
    )
    is_active: Optional[bool] = Field(
        None,
        description="Flag indicating if the user is active."
    )


class UserResponseSchema(UserBaseSchema):
    """
    Schema for returning user data in responses.

    Inherits from `UserBaseSchema` and adds fields for the user's `id`, `is_active` status,
    creation and modification timestamps, last login timestamp, and profile image.

    Attributes:
        id (UUID4): Unique ID of the user.
        is_active (bool): Flag indicating if the user is active.
        created (datetime): Timestamp when the user was created.
        modified (datetime): Timestamp when the user was last modified.
        last_login (Optional[datetime]): Timestamp of the user's last login (optional).
        image (Optional[str]): URL or path to the user's profile image (optional).
    """
    id: UUID4 = Field(
        ...,
        description="Unique ID of the user."
    )
    is_active: bool = Field(
        ...,
        description="Flag indicating if the user is active."
    )
    created: datetime = Field(
        ...,
        description="Timestamp when the user was created."
    )
    modified: datetime = Field(
        ...,
        description="Timestamp when the user was last modified."
    )
    last_login: Optional[datetime] = Field(
        None,
        description="Timestamp of the user's last login."
    )
    image: Optional[str] = Field(
        None,
        description="URL or path to the user's profile image."
    )

    class Config:
        from_attributes = True
