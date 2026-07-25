from app.services.crime_intelligence import clean_crime_dataframe


def test_clean_crime_dataframe_removes_duplicates_and_invalid_coordinates():
    data = [
        {
            "id": 1,
            "date": "2024-01-10 09:30:00",
            "primary_type": "THEFT",
            "description": "OVER $500",
            "latitude": 41.88,
            "longitude": -87.63,
            "district": 1,
            "ward": 4,
        },
        {
            "id": 1,
            "date": "2024-01-10 09:30:00",
            "primary_type": "THEFT",
            "description": "OVER $500",
            "latitude": 41.88,
            "longitude": -87.63,
            "district": 1,
            "ward": 4,
        },
        {
            "id": 2,
            "date": "2024-01-11 10:00:00",
            "primary_type": "BATTERY",
            "description": "SIMPLE",
            "latitude": 999,
            "longitude": -87.63,
            "district": 2,
            "ward": 5,
        },
        {
            "id": 3,
            "date": None,
            "primary_type": "ASSAULT",
            "description": "AGGRAVATED",
            "latitude": 41.90,
            "longitude": -87.70,
            "district": 3,
            "ward": 6,
        },
        {
            "id": 4,
            "date": "2024-01-13 08:00:00",
            "primary_type": "BURGLARY",
            "description": "RESIDENTIAL",
            "latitude": 41.91,
            "longitude": -87.68,
            "district": 4,
            "ward": 7,
        },
    ]

    cleaned = clean_crime_dataframe(data)

    assert len(cleaned) == 2
    assert len({record["id"] for record in cleaned}) == 2
    assert all(41.6 <= record["latitude"] <= 42.0 for record in cleaned)
    assert all(-87.9 <= record["longitude"] <= -87.5 for record in cleaned)
    assert all("year" in record for record in cleaned)
