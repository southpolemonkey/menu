from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    id: str = Field(...)
    username: str = EmailStr(...)
    password: str = Field(...)
    createAt: str
    updateAt: str

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "username": "user@exampl.com",
                "password": "randomtexthere",
            }
        }

class UpdateUserSchema(BaseModel):
    password: str = Optional[str]