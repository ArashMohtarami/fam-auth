from typing import List

from starlette import status
from fastapi import Depends, APIRouter

from src.repository.data_access.manager.user import UserManager
from src.dependencies import get_user_manager
from src.schemas import UserCreateSchema, UserResponseSchema


router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/users/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def register_new_user(
    create_user: UserCreateSchema,
    user_manager: UserManager = Depends(get_user_manager)
):
    """
    Register a new user.

    This endpoint allows the creation of a new user by providing the necessary 
    user details such as `username`, `email`, `password`, etc.

    Args:
        create_user (UserCreateSchema): The user data required to create a new user.
        user_manager (UserManager): The user manager service responsible for user operations.

    Returns:
        UserResponseSchema: The newly created user details, including the `id`, `created`, and `modified` timestamps.
    
    Status Codes:
        201: User created successfully.
        404: Not found (if user manager is unavailable).
    """
    user = await user_manager.create_user(create_user)
    return user


@router.get("/users/", response_model=List[UserResponseSchema], status_code=status.HTTP_200_OK)
async def get_users(
    user_manager: UserManager = Depends(get_user_manager),
):
    """
    Get all users.

    This endpoint retrieves a list of all users from the database.

    Args:
        user_manager (UserManager): The user manager service responsible for retrieving user data.

    Returns:
        List[UserResponseSchema]: A list of user details, including `id`, `email`, `first_name`, `last_name`, etc.

    Status Codes:
        200: Successfully retrieved the list of users.
        404: Not found (if user manager is unavailable).
    """
    user = await user_manager.get_all_users()
    return user


@router.get("/users/{id}", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_user(
    id: str,
    user_manager: UserManager = Depends(get_user_manager),
):
    """
    Get a single user by ID.

    This endpoint retrieves a specific user by their unique ID.

    Args:
        id (str): The unique ID of the user to retrieve.
        user_manager (UserManager): The user manager service responsible for retrieving user data.

    Returns:
        UserResponseSchema: The user details, including `id`, `email`, `first_name`, `last_name`, etc.

    Status Codes:
        200: Successfully retrieved the user.
        404: User not found (if no user with the provided ID exists).
    """
    user = await user_manager.get_user_by_id(id)
    return user
