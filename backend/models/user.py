from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    id: str
    username: str
    password: str
    createAt: str
    updateAt: str

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "username": "user@exampl.com",
                "password": "randomtexthere",
                "createAt": "2021-08-03",
                "createAt": "2021-08-11",
            }
        }

class UpdateUserSchema(BaseModel):
    password: str = Optional[str]