from pydantic import BaseModel, EmailStr, Field, UUID4
from datetime import datetime, date
from typing import Optional


class UserBaseSchema(BaseModel):
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
    password: str = Field(
        ...,
        description="Password for the user."
    )


class UserUpdateSchema(UserBaseSchema):
    password: Optional[str] = Field(
        None,
        description="Password for the user."
    )
    is_active: Optional[bool] = Field(
        None,
        description="Flag indicating if the user is active."
    )


class UserPatchSchema(BaseModel):
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
