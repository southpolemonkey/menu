from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException


from backend.db.user import (
    add_user,
    find_user,
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

SECRET = "super-secret-key"
manager = LoginManager(SECRET, '/login', use_cookie=True)

@router.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = find_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data={'sub': email}
    )

    manager.set_cookie(response, access_token)
    return {'token': access_token}

@router.get("/", response_description="get_user")
def get_all_user():
    pass

@router.get("/{id}", response_description="fetch details of single user")
def get_user(id=Depends(manager)):
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

@router.delete("/{id}", response_description="delete user")
def delete_user(id: str):
    pass


