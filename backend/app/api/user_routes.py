from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse,UserLogin
from app.services import user_service
from app.core.security import create_access_token

router = APIRouter()


# CREATE USER
@router.post("/register", response_model=UserResponse)
def create_user(user: UserCreate):
    return user_service.create_user(user)



# GET ALL USERS
@router.get("/", response_model=list[UserResponse])
def get_users():
    return user_service.get_users()


# GET ONE USER
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = user_service.get_user(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# DELETE USER
@router.delete("/{user_id}")
def delete_user(user_id: int):
    user = user_service.delete_user(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}