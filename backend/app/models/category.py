from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # One category → many recipes
    recipes = relationship("Recipe", back_populates="category")