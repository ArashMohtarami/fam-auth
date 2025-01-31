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

    user = await user_manager.create_user(create_user)
    return user


@router.get("/users/", response_model=List[UserResponseSchema,], status_code=status.HTTP_200_OK)
async def get_users(
    user_manager: UserManager = Depends(get_user_manager),
    ):

    user = await user_manager.get_all_users()
    return user


@router.get("/users/{id}", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_user(
    id: str,
    user_manager: UserManager = Depends(get_user_manager),
    ):

    user = await user_manager.get_user_by_id(id)
    return user
