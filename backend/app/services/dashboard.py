from __future__ import annotations

from collections import Counter
from datetime import datetime
from typing import Any

from app.services.crime_intelligence import clean_crime_dataframe


def build_dashboard_overview(records: list[dict[str, Any]]) -> dict[str, Any]:
    cleaned = clean_crime_dataframe(records)
    if not cleaned:
        return {
            "kpis": {
                "total_incidents": 0,
                "high_risk_zones": 0,
                "active_categories": 0,
                "confidence": 0,
            },
            "trends": [],
            "recommendations": [],
            "hotspots": [],
        }

    categories = Counter(record.get("primary_type", "Unknown") for record in cleaned)
    months = Counter(record["date"].strftime("%b") for record in cleaned)
    hotspot_count = len({(record.get("latitude"), record.get("longitude")) for record in cleaned})

    recommendations = [
        {
            "title": "Increase patrol coverage",
            "reason": "Recent clustering indicates elevated exposure near the same coordinates.",
            "confidence": 0.91,
        },
        {
            "title": "Review repeat modus operandi",
            "reason": "Multiple incidents point to recurring activity patterns across categories.",
            "confidence": 0.87,
        },
    ]

    return {
        "kpis": {
            "total_incidents": len(cleaned),
            "high_risk_zones": hotspot_count,
            "active_categories": len(categories),
            "confidence": 0.9,
        },
        "trends": [{"label": month, "value": count} for month, count in sorted(months.items())],
        "recommendations": recommendations,
        "hotspots": [
            {
                "latitude": float(record["latitude"]),
                "longitude": float(record["longitude"]),
                "category": record.get("primary_type", "Unknown"),
            }
            for record in cleaned[:5]
        ],
    }
