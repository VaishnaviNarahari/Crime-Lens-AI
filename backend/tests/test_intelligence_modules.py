from app.services.dashboard import build_dashboard_overview


def test_build_dashboard_overview_exposes_kpis_and_trends():
    records = [
        {
            "id": 1,
            "date": "2024-01-10 09:30:00",
            "primary_type": "Theft",
            "latitude": 41.88,
            "longitude": -87.63,
        },
        {
            "id": 2,
            "date": "2024-01-11 10:00:00",
            "primary_type": "Battery",
            "latitude": 41.87,
            "longitude": -87.62,
        },
        {
            "id": 3,
            "date": "2024-02-10 12:00:00",
            "primary_type": "Assault",
            "latitude": 41.89,
            "longitude": -87.64,
        },
    ]

    overview = build_dashboard_overview(records)

    assert overview["kpis"]["total_incidents"] == 3
    assert overview["kpis"]["high_risk_zones"] >= 1
    assert overview["trends"][0]["label"] in {"Jan", "Feb"}
    assert overview["recommendations"]
