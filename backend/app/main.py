from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse

from app.services.crime_intelligence import clean_crime_dataframe, generate_explainable_summary
from app.services.dashboard import build_dashboard_overview
from app.services.predictive import build_predictive_intelligence

app = FastAPI(title="CrimeLens AI API", version="0.1.0")

ROOT_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIST_DIR = ROOT_DIR / "frontend" / "dist"
INDEX_HTML_PATH = FRONTEND_DIST_DIR / "index.html"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> HTMLResponse:
    if INDEX_HTML_PATH.exists():
        return HTMLResponse(INDEX_HTML_PATH.read_text(encoding="utf-8"))
    return HTMLResponse("<h1>CrimeLens AI</h1><p>Frontend build not found.</p>")


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
