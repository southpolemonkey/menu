from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from backend.database import (
    add_user,
    update_user,
)

from backend.models.user import (
    UserSchema,
    UpdateUserSchema,
)
from backend.models.common import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.get("/", response_description="get_user")
def get_all_user():
    pass

@router.get("/{id}", response_description="fetch details of single user")
def find_user(id: str):
    if user := find_user(id):
        return ResponseModel(user, "fetch user")
    return ErrorResponseModel(
        "Error occurred", 404, "User with id {} doesn't exist".format(id)
    )

@router.post("/", response_description="create new user")
def create_new_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = add_user(user)
    return ResponseModel(new_user, "New User created successfully")

@router.put("/{id}", response_description="update user details")
def update_user(id: str, req: UpdateUserSchema = Body(...)):
    pass

