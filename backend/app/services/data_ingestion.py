from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Any


def load_crime_dataset(dataset_path: str | Path | None = None, limit: int | None = None) -> list[dict[str, Any]]:
    """Load crime incident records from a CSV file or fall back to bundled sample data."""
    if dataset_path is None:
        dataset_path = Path(__file__).resolve().parents[2] / "data" / "chicago_crimes_sample.csv"
    else:
        dataset_path = Path(dataset_path)

    if dataset_path.exists():
        with dataset_path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    else:
        rows = []

    if limit is not None:
        rows = rows[:limit]

    if rows:
        return rows

    return [
        {
            "id": 1001,
            "date": "2024-01-10 09:30:00",
            "primary_type": "Theft",
            "description": "Over $500",
            "latitude": 41.88,
            "longitude": -87.63,
        },
        {
            "id": 1002,
            "date": "2024-01-11 10:15:00",
            "primary_type": "Battery",
            "description": "Simple battery",
            "latitude": 41.87,
            "longitude": -87.62,
        },
        {
            "id": 1003,
            "date": "2024-01-12 11:45:00",
            "primary_type": "Assault",
            "description": "Aggravated",
            "latitude": 41.89,
            "longitude": -87.64,
        },
    ]
