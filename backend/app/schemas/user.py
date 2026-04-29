from pydantic import BaseModel, EmailStr,Field

# create user validation
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

# login schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str
