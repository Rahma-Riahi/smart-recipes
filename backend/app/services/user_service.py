from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password ,verify_password
from fastapi import  HTTPException


def create_user(data):
    db = SessionLocal()
    hashed_pw = hash_password(data.password)
     # check if user exists
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        name=data.name,
        email=data.email,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()
    return new_user


def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users


def get_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user


def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        db.delete(user)
        db.commit()

    db.close()
    return user




# LOGIN
def authenticate_user( email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user