from pydantic import BaseModel, field_validator
from datetime import datetime


class MPGLog(BaseModel):
    registration: str
    date: str
    litres: float
    miles: float
    mpg: float
    total_cost: float

    @field_validator('date', mode='after')
    @classmethod
    def is_in_correct_date_format(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except Exception:
            raise ValueError("Date must be in the format YYYY-MM-DD")
        return value
