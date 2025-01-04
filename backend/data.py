import json
from pathlib import Path
from typing import Any


def load_data(file_name: str) -> list[dict[str, Any]]:
    with open(Path.cwd() / "backend" / "data" / file_name) as f:
        data = json.load(f)
    return data


MODEL_RUNS = load_data("model_runs.json")
FINAL_RUNS = load_data("final_runs.json")
