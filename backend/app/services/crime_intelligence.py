from __future__ import annotations

from collections import Counter
from datetime import datetime
from typing import Any


def clean_crime_dataframe(raw: list[dict[str, Any]] | None) -> list[dict[str, Any]]:
    """Clean and standardize crime incident data for intelligence analysis."""
    if not raw:
        return []

    cleaned: list[dict[str, Any]] = []
    seen_ids: set[Any] = set()

    for record in raw:
        normalized = {key.strip().lower(): value for key, value in record.items()}
        record_id = normalized.get("id")
        if record_id is None or record_id in seen_ids:
            continue
        seen_ids.add(record_id)

        date_value = normalized.get("date")
        primary_type = normalized.get("primary_type")
        latitude = normalized.get("latitude")
        longitude = normalized.get("longitude")

        if not date_value or not primary_type or latitude is None or longitude is None:
            continue

        try:
            parsed_date = datetime.fromisoformat(str(date_value).replace("Z", "+00:00"))
        except ValueError:
            try:
                parsed_date = datetime.strptime(str(date_value), "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue

        try:
            lat = float(latitude)
            lon = float(longitude)
        except (TypeError, ValueError):
            continue

        if not (40.0 <= lat <= 45.0 and -90.0 <= lon <= -80.0):
            continue

        normalized_record = dict(normalized)
        normalized_record["date"] = parsed_date
        normalized_record["latitude"] = lat
        normalized_record["longitude"] = lon
        normalized_record["year"] = parsed_date.year
        normalized_record["month"] = parsed_date.month
        normalized_record["day_of_week"] = parsed_date.strftime("%A")
        normalized_record["primary_type"] = str(primary_type).title()
        cleaned.append(normalized_record)

    return cleaned


def generate_explainable_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Create an explainable intelligence summary for a crime dataset."""
    if not records:
        return {"total_incidents": 0, "top_categories": [], "hotspots": []}

    categories = Counter(record.get("primary_type", "Unknown") for record in records)
    hotspots = Counter((record.get("latitude"), record.get("longitude")) for record in records)

    return {
        "total_incidents": int(len(records)),
        "top_categories": [{"category": category, "count": int(count)} for category, count in categories.most_common(5)],
        "hotspots": [
            {"latitude": float(lat), "longitude": float(lon), "incident_count": int(count)}
            for (lat, lon), count in hotspots.most_common(5)
        ],
    }
