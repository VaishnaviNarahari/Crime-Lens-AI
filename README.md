# CrimeLens AI

CrimeLens AI is a production-oriented intelligence platform for the Karnataka Crime Intelligence Operating System. It combines an extendable crime data cleaning pipeline with a FastAPI backend and a React-based command-center shell for explainable investigation workflows.

## Architecture

- Backend: FastAPI service for intelligence endpoints
- Data layer: cleaning and normalization utilities for crime incident data
- Frontend: React/Vite command center for operational visualization and analysis
- Testing: pytest-based regression tests for preprocessing pipelines

## Project structure

- backend/app/services: core cleaning and intelligence logic
- backend/tests: regression tests for preprocessing
- frontend/src: React UI shell and styles

## Running locally

### Backend

```bash
cd backend
python -m pip install fastapi==0.115.0 uvicorn==0.32.0 pytest==8.3.4
python -m uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Current capabilities

- Explainable crime summary generation
- Data cleaning for incident records
- A modular frontend shell for future GIS, graph, and alert modules

## Next steps

1. Add PostgreSQL and Neo4j integrations
2. Connect real FIR data and GIS mapping layers
3. Implement predictive models with explainable outputs
4. Add network analysis, alerting, and role-based dashboards
