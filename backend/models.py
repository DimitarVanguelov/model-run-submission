from datetime import date, datetime

from pydantic import UUID4, BaseModel


class ModelRun(BaseModel):
    run_id: UUID4
    valuation_date: date
    model_result: float


class FinalRun(BaseModel):
    run_id: UUID4
    user_submitted: str
    datetime_submitted: datetime
