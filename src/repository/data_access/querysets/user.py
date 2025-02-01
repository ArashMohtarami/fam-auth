import os
import re
import shutil

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy import update, delete
from datetime import datetime, timezone
from passlib.context import CryptContext
from fastapi import UploadFile

from src.models.user import User
from src.schemas.user import UserCreateSchema, UserUpdateSchema
from src.utils.regular_expressions import PHONE_PATTERN
from src.exceptions import (
    ImageUploadError,
    UserNotFoundError,
    PasswordMatchError,
    InvalidPhoneNumberError,
    PasswordConfirmationError,
    UsernameAlreadyExistsError,
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserQuery:
    """
    A class to interact with the user-related database queries.

    This class provides methods to query, create, and manipulate user data
    within the database using SQLAlchemy ORM and asynchronous session handling.
    """

    def __init__(self, db: AsyncSession):
        """
        Initializes the UserQuery class with the database session.

        :param db: The SQLAlchemy asynchronous session.
        :type db: AsyncSession
        """
        self.db = db

    async def get_user_by_id(self, user_id: int) -> User:
        """
        Retrieve a user by their unique ID.

        :param user_id: The ID of the user.
        :type user_id: int
        :raises UserNotFoundError: If the user does not exist.
        :return: The user object.
        :rtype: User
        """
        result = await self.db.execute(select(User).filter(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found.")

        return user

    async def get_user_by_email(self, email: str) -> User:
        """
        Retrieve a user by their email address.

        :param email: The email of the user.
        :type email: str
        :raises UserNotFoundError: If the user does not exist.
        :return: The user object.
        :rtype: User
        """
        result = await self.db.execute(select(User).filter(User.email == email))
        user = result.scalar_one_or_none()

        if not user:
            raise UserNotFoundError(f"User with email {email} not found.")

        return user

    async def register_new_user(self, user_data: UserCreateSchema) -> User:
        """
        Register a new user after validating username uniqueness, password confirmation,
        and phone number format.

        phone number formats are:
            Valid examples:
                - +14155552671 (US)
                - +919876543210 (India)
                - +447911123456 (UK)
                - +989195876954 (IR)
            Invalid examples:
                - 123456 (Missing country code)
                - +1 (415) 555-2671 (Contains spaces/parentheses)
                - 415-555-2671 (Not in international format)

        :param user_data: The data required to create a new user.
        :type user_data: UserCreateSchema
        :raises UsernameAlreadyExistsError: If the username is already taken.
        :raises PasswordConfirmationError: If passwords do not match.
        :raises InvalidPhoneNumberError: If the phone number format is incorrect.
        :return: The newly created user object.
        :rtype: User
        """
        result = await self.db.execute(
            select(User).where(User.username == user_data.username)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise UsernameAlreadyExistsError(
                f"Username '{user_data.username}' is already taken. Choose another."
            )

        if user_data.password != user_data.confirm_password:
            raise PasswordConfirmationError(
                "Password and confirmation password do not match."
            )

        phone_pattern = PHONE_PATTERN
        if user_data.phone_number and not re.match(
            phone_pattern, user_data.phone_number
        ):
            raise InvalidPhoneNumberError(
                "Invalid phone number format. Use international format (e.g., +14155552671)."
            )

        hashed_password = pwd_context.hash(user_data.password)

        user_data_dict = user_data.model_dump(exclude={"confirm_password"})
        user_data_dict["password"] = hashed_password

        new_user = User(**user_data_dict)
        self.db.add(new_user)

        try:
            await self.db.commit()
            await self.db.refresh(new_user)
            return new_user
        except IntegrityError:
            await self.db.rollback()
            raise ValueError("Failed to register user due to a database error.")

    async def login(self, email: str, password: str) -> User:
        """
        Authenticate a user and update the last login timestamp.

        :param email: The user's email address.
        :type email: str
        :param password: The user's password.
        :type password: str
        :return: The authenticated user object or None if credentials are invalid.
        :rtype: User or None
        """
        user = await self.get_user_by_email(email)
        if not user or not pwd_context.verify(password, user.password):
            return None

        user.last_login = datetime.now(timezone.utc)
        await self.db.commit()
        return user

    async def change_password(
        self, user_id: int, new_password: str, confirm_password: str
    ) -> None:
        """
        Update the user's password after performing necessary checks.

        :param user_id: The ID of the user.
        :type user_id: int
        :param new_password: The new password to be set.
        :type new_password: str
        :param confirm_password: The confirmation password to verify correctness.
        :type confirm_password: str
        :raises PasswordMatchError: If the new password is the same as the old one.
        :raises PasswordConfirmationError: If the new password and confirmation do not match.
        """
        result = await self.db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if not user:
            raise ValueError("User not found")

        if pwd_context.verify(new_password, user.password):
            raise PasswordMatchError(
                "New password cannot be the same as the old password."
            )

        if new_password != confirm_password:
            raise PasswordConfirmationError(
                "New password and confirmation password do not match."
            )

        hashed_password = pwd_context.hash(new_password)
        stmt = update(User).where(User.id == user_id).values(password=hashed_password)
        await self.db.execute(stmt)
        await self.db.commit()

    async def change_username(self, user_id: int, new_username: str) -> None:
        """
        Update the user's username after checking for duplicates.

        :param user_id: The ID of the user.
        :type user_id: int
        :param new_username: The new username to be set.
        :type new_username: str
        :raises UsernameAlreadyExistsError: If the chosen username is already taken.
        """
        result = await self.db.execute(
            select(User).where(User.username == new_username)
        )
        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise UsernameAlreadyExistsError(
                f"Username '{new_username}' is already taken. Choose another."
            )

        stmt = update(User).where(User.id == user_id).values(username=new_username)
        await self.db.execute(stmt)
        await self.db.commit()

    async def change_image(self, user_id: int, image: UploadFile) -> str:
        """
        Upload and update the user's profile image.

        :param user_id: The ID of the user.
        :type user_id: int
        :param image: The uploaded image file.
        :type image: UploadFile
        :raises ImageUploadError: If the image upload fails.
        :return: The new image URL.
        :rtype: str
        """
        upload_dir = "static/uploads/profile_images/"
        os.makedirs(upload_dir, exist_ok=True)

        image_path = os.path.join(upload_dir, f"user_{user_id}_{image.filename}")

        try:
            with open(image_path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)

            stmt = update(User).where(User.id == user_id).values(image=image_path)
            await self.db.execute(stmt)
            await self.db.commit()
            return image_path
        except Exception as e:
            raise ImageUploadError(f"Failed to upload image: {str(e)}")
