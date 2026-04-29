from fastapi import APIRouter, HTTPException
from app.schemas.user import UserLogin
from app.services import user_service
from app.core.security import create_access_token
from app.db.database import SessionLocal

router = APIRouter()
db = SessionLocal()



# LOGIN

@router.post("/login")
def login(user: UserLogin):
    db_user = user_service.authenticate_user(user.email, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }