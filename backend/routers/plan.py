from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from backend.models.plan import (
    WeeklyPlanSchema,
    PartyPlanSchema,
)

from backend.models.common import (
    ErrorResponseModel,
    ResponseModel,
)

from backend.db.menu import (
    add_menu,
    update_menu,
    delete_menu,
)

router = APIRouter()

"""
/plan/weekly/
/plan/party/
"""

@router.get("/", response_description="retrieve all plans")
def get_all_plan():
    plans = ""
    return ResponseModel(plans, "Retrieve all plans")

@router.get("/", response_description="retrieve a single plan")
def get_single_plan(id: str):
    plan = ""
    return ResponseModel(plan, "Retrieve plan")