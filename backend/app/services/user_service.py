from app.db.database import SessionLocal
from app.models.user import User

def create_user(data):
    db = SessionLocal()

    new_user = User(
        name=data.name,
        email=data.email,
        password=data.password
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