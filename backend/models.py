from datetime import datetime

from pydantic import UUID4, BaseModel


class ModelRun(BaseModel):
    run_id: UUID4
    model_result: float


class FinalRun(BaseModel):
    run_id: UUID4
    user_submitted: str
    datetime_submitted: datetime
