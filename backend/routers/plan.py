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

router = APIRouter()

"""
/plan/weekly/
/plan/party/
"""

@router.get("/weekly", response_description="retrieve all weekly plans")
def get_all_weekly_plan():
    plans = []
    return ResponseModel(plans, "Retrieve all plans")

@router.get("/weekly/{id}", response_description="retrieve a single weekly plan")
def get_single_weekly_plan(id: str):
    plan = []
    return ResponseModel(plan, "Retrieve plan")
