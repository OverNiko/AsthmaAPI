from typing import Annotated
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]
    name: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str