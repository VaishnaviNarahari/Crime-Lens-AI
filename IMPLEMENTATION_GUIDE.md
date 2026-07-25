# Implementation Guide

# 1. Development Roadmap

## Phase 1 – Project Setup

- Create monorepo
- React + Vite
- FastAPI
- PostgreSQL
- Neo4j
- Docker
- Git

## Phase 2 – Database

- PostgreSQL
- SQLAlchemy models
- Alembic
- seed scripts

## Phase 3 – Authentication

- JWT
- login
- roles
- audit logs

## Phase 4 – Dataset Import

- Chicago CSV
- cleaning
- validation
- feature engineering
- database loading

## Phase 5 – Dashboard

- KPIs
- charts
- AI cards
- recent crimes

## Phase 6 – Crime Map

- Leaflet
- heatmaps
- timeline
- filters

## Phase 7 – Network Intelligence

- Neo4j
- React Flow
- relationship explorer

## Phase 8 – Prediction Engine

- hotspot prediction
- crime forecast
- risk score
- SHAP

## Phase 9 – AI Copilot

- natural language search
- case summaries
- pattern discovery

## Phase 10 – Reports

- PDF
- CSV
- Excel

# 2. REST API Structure

## Authentication

- POST /api/auth/login
- POST /api/auth/register
- GET /api/auth/profile

## Crimes

- GET /api/crimes
- GET /api/crimes/{id}
- POST /api/crimes

## Dashboard

- GET /api/dashboard/overview
- GET /api/dashboard/kpis
- GET /api/dashboard/trends

## Map

- GET /api/map/crimes
- GET /api/map/heatmap

## Predictions

- GET /api/predict/hotspots
- GET /api/predict/risk

## AI Assistant

- POST /api/chat
- POST /api/chat/summary

# 3. Frontend Component Tree

```
App
├── Sidebar
├── Navbar
├── Dashboard
├── Map
├── AI Copilot
├── Network Graph
├── Charts
├── Reports
└── Settings
```

# 4. Cursor Prompt Strategy

Work feature by feature.

Use a build sequence like:

1. Dashboard
2. Crime Map
3. Prediction Module
4. Network Intelligence
5. AI Copilot

# 5. Final Folder Structure

```
CrimeLensAI/
├── frontend/
├── backend/
├── machine-learning/
├── neo4j/
├── database/
├── docs/
├── scripts/
├── tests/
├── docker-compose.yml
├── README.md
└── .env.example
```
