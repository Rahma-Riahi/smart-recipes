from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user
from app.api.user_routes import router as user_router


#Create tables in DB
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Recipes API")


app.include_router(user_router, prefix="/users", tags=["Users"])