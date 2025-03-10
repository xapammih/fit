from fastapi import APIRouter

router = APIRouter()


@router.post("add_calories")
def add_calories(food_name: str, serving_size: float, calories: float):
    ...
