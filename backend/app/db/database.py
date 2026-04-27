from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

#get db url
DATABASE_URL = os.getenv("DATABASE_URL")



#connect and manage communication with db
engine = create_engine(DATABASE_URL)

#create db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# defines database tables
Base = declarative_base()