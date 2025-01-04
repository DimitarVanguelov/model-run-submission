from datetime import date, datetime
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import UUID4

from .data import FINAL_RUNS, MODEL_RUNS
from .models import FinalRun, ModelRun

app = FastAPI()


@app.get("/")
def root() -> dict[str, Path]:
    """Return the current working directory."""
    return {"message": Path.cwd()}


@app.get("/modelruns")
def read_runs(run_id: UUID4 | None = None) -> list[ModelRun]:
    """Return a list of model runs. Optionally supply a `run_id` to filter by."""
    runs = [
        ModelRun(**run)
        for run in MODEL_RUNS
        if not run_id or run.get("run_id") == str(run_id)
    ]
    if not runs:
        raise HTTPException(status_code=404, detail="Run not found")
    return runs


def get_date(date_str: Any) -> date:
    return datetime.fromisoformat(date_str).date()


@app.get("/finalruns")
def read_final_runs(
    run_id: UUID4 | None = None,
    user_submitted: str | None = None,
    date_submitted: date | None = None,
) -> list[FinalRun]:
    """
    Return a list of final runs. Optionally supply a `run_id`,
    `user_submitted`, and/or `date_submitted` to filter by.
    """
    runs = [
        FinalRun(**run)
        for run in FINAL_RUNS
        if (not run_id or run.get("run_id") == str(run_id))
        and (not user_submitted or run.get("user_submitted") == user_submitted)
        and (
            not date_submitted
            or get_date(run.get("datetime_submitted")) == date_submitted
        )
    ]
    if not runs:
        raise HTTPException(status_code=404, detail="Run not found")
    return runs


@app.post("/finalruns")
def create_final_run(final_run: FinalRun) -> FinalRun:
    """Create a new final run."""
    FINAL_RUNS.append(final_run.model_dump())
    return final_run
