# CrimeLens AI

### Karnataka Crime Intelligence Operating System (KCIOS)

# Vision

The Karnataka State Police currently rely on traditional FIR systems, fragmented records, and spreadsheet-based reporting.

The objective is to build a next-generation AI-powered Crime Intelligence Platform that transforms crime records into actionable intelligence.

The platform should assist

- Police Officers
- Investigators
- Intelligence Analysts
- District SPs
- SCRB Officers

in making faster, smarter, and evidence-driven decisions.

# Primary Objectives

The system should

✅ Detect Crime Hotspots

✅ Predict Future Crime

✅ Discover Hidden Criminal Networks

✅ Analyze Crime Trends

✅ Detect Repeat Offenders

✅ Discover Modus Operandi

✅ Generate AI Investigation Reports

✅ Explain Predictions

✅ Recommend Police Actions

# Primary Dataset

Use

**Chicago Crime Dataset**

as the historical crime dataset.

The system should automatically preprocess

- Missing values
- Duplicate records
- Invalid GPS
- Feature extraction

Generate

Hour

Weekday

Weekend

Month

Season

Time Bucket

Severity Score

Risk Index

Crime Frequency

Location Density

Hotspot Cluster

# Database Design

Use

### PostgreSQL

for operational data.

### Neo4j

for relationship intelligence.

The official Karnataka Police FIR ER Diagram should be used as the operational database model, with entities such as `CaseMaster`, `Victim`, `Accused`, `Complainant`, `Employee`, `District`, `Unit`, and related tables forming the foundation. AI-specific tables (predictions, alerts, model outputs) should extend this schema rather than replace it.

# AI Layer

The platform should support

## Machine Learning

Random Forest

XGBoost

Isolation Forest

DBSCAN

KMeans

Time Series Forecasting

Graph Analytics

SHAP Explainability

# UI Philosophy

Never create

❌ Bootstrap Dashboard

❌ Generic Admin Panel

Instead create

✔ Intelligence Command Center

# Theme

Dark

Glassmorphism

Blue

Purple

Minimal

Professional

Military-grade aesthetics

# User Roles

Administrator

SCRB Intelligence Officer

District SP

Inspector

Police Constable

Crime Analyst

Each role should see different dashboards.

# Authentication

JWT

Role-Based Access

Password Hashing

Audit Logs

Session Management

# Dashboard

The dashboard should immediately answer

How many crimes happened today?

Where?

Why?

What pattern?

What prediction?

What recommendation?

# Include

Interactive Karnataka Map

Heatmap

Crime Timeline

Risk Meter

AI Recommendations

Recent FIR

Live Alerts

Crime Trends

Crime Categories

Officer Activity

# Crime Map

Use

Leaflet

or

Mapbox

Features

Heatmaps

Timeline Replay

Crime Pins

Police Stations

Satellite View

District Filters

Crime Filters

Hover Popups

Animated Clusters

# Network Intelligence

Build an interactive force-directed graph.

Nodes

Cases

Accused

Victims

Vehicles

Phones

Weapons

Police Stations

Locations

Edges

Known Associate

Shared FIR

Shared Vehicle

Shared Phone

Same Address

Repeat Offender

Graph Algorithms

PageRank

Community Detection

Shortest Path

Influence Score

# Predictive Intelligence

Predict

Tomorrow's Hotspots

High-Risk Areas

Emerging Crime Types

Patrol Recommendation

Officer Allocation

Each prediction should include

Probability

Confidence

Historical Trend

SHAP Explanation

Police Recommendation

# AI Investigation Assistant

LLM-powered chatbot.

Capabilities

Natural Language Search

Case Summary

Crime Pattern Explanation

Recommendation Generation

District Report

Officer Report

Examples

Show robbery cases near schools.

Predict tomorrow's hotspot.

Find repeat offenders.

Explain today's anomaly.

Generate FIR summary.

# Smart Alerts

Generate alerts when

Crime Spike

Repeat Offender

Gang Activity

High Risk Zone

Anomaly

Prediction Confidence >90%

# Reports

Generate

PDF

Excel

CSV

AI Intelligence Brief

District Report

Monthly Crime Report

# Security

Encrypted JWT

Input Validation

Rate Limiting

Audit Logs

Secure APIs

# Technology

Frontend

React

TypeScript

Tailwind

Framer Motion

React Flow

Leaflet

Recharts

Backend

FastAPI

Python

SQLAlchemy

PostgreSQL

Neo4j

Redis

Machine Learning

scikit-learn

XGBoost

NetworkX

SHAP

Pandas

NumPy

# Folder Structure

```
CrimeLensAI/

frontend/

backend/

database/

machine-learning/

neo4j/

docker/

docs/

api/

scripts/

tests/
```

# Final Goal

Build software that looks like an Intelligence Command Center used by a state police agency rather than a college dashboard.

# Important Cursor Rules

At the end of your prompt, always append this:

```
IMPORTANT:

Do NOT build the whole application in one response.

Work module by module.

Before generating code:

1. Explain the architecture.

2. Explain the folder structure.

3. List dependencies.

4. Create reusable components.

5. Build feature by feature.

6. Do not generate placeholder UI.

7. Never stop after creating only the landing page.

8. Every page should be functional.

9. Use real charts.

10. Use real maps.

11. Connect everything with APIs.

12. Follow production architecture.

13. Write clean, commented code.

14. Never sacrifice quality for speed.

Think like a Senior Engineer at Palantir building intelligence software.
```
