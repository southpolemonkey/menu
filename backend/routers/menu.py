from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from backend.database import (
    add_menu,
    find_menu,
    all_menu,
    delete_menu,
    update_menu,
)

from backend.models.menu import (
    MenuSchema,
    UpdateMenuSchema,
)

from backend.models.common import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.get("/", response_description="retrieve all menu")
def get_all_menu():
    menus = all_menu()
    return ResponseModel(menus, "Retrieve all menu")

@router.get("/{id}", response_description="retrieve a singe menu")
def get_single_menu(id: str):
    if menu := find_menu(id):
        return ResponseModel(menu, "retrieve menu")
    return ErrorResponseModel(
        "Error occurred", 404, "Menu with id {} doesn't exist".format(id)
    )

@router.post("/", response_description="create new menu")
def add_menu_data(menu: MenuSchema = Body(...)):
    menu = jsonable_encoder(menu)
    new_menu = add_menu(menu)
    return ResponseModel(new_menu, "Menu added successfully")

@router.put("/{id}", response_description="update menu")
def update_menu_date(id: str, req: UpdateMenuSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = update_menu(id, req)
    if updated_student:
        return ResponseModel(
            "Menu with ID: {} name update is successful".format(id),
            "Menu {} updated successfully".format(id),
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the menu data.",
    )


@router.delete("/{id}", response_description="Menu data deleted")
def delete_menu_data(id: str):
    if delete_menu(id):
        return ResponseModel(
            "Menu removed successfully",
            "Deleted menu with id {}".format(id)
        )
    return ErrorResponseModel(
        "Error occurred", 404, "Menu with id {} doesn't exist".format()
    )

