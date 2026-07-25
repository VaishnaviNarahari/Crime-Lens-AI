from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.crime_intelligence import clean_crime_dataframe, generate_explainable_summary
from app.services.dashboard import build_dashboard_overview
from app.services.predictive import build_predictive_intelligence

app = FastAPI(title="CrimeLens AI API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "crime-intelligence-api"}


@app.post("/intelligence/summary")
def intelligence_summary(payload: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    records = payload.get("records", [])
    if not records:
        return {"total_incidents": 0, "top_categories": [], "hotspots": []}

    cleaned = clean_crime_dataframe(records)
    return generate_explainable_summary(cleaned)


@app.post("/dashboard/overview")
def dashboard_overview(payload: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    records = payload.get("records", [])
    return build_dashboard_overview(records)


@app.post("/predictive/intelligence")
def predictive_intelligence(payload: dict[str, list[dict[str, object]]]) -> dict[str, object]:
    records = payload.get("records", [])
    return build_predictive_intelligence(records)
