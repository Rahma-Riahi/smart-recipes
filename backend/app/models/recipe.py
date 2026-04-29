from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ingredients = Column(Text)
    steps = Column(Text, nullable=False)
    cooking_time = Column(Integer, nullable=True)
    pictures = Column(Text, nullable=False)
    # Foreign key (link to user)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Foreign key (link to categorie)
    category_id  = Column(Integer, ForeignKey("categories.id"))
    
    # Relationships
    owner = relationship("User", back_populates="recipes")
    category = relationship("Category", back_populates="recipes")

