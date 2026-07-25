# Database, Data Pipeline & AI Architecture

# 1. Overall Data Flow

```
                 Chicago Crime Dataset
                         │
                         ▼
             Data Cleaning & Validation
                         │
                         ▼
              Feature Engineering Pipeline
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
  PostgreSQL Database             Neo4j Knowledge Graph
        │                                 │
        └──────────────┬──────────────────┘
                       ▼
              FastAPI Intelligence Layer
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Dashboard      AI Predictions   Investigation AI
```

# 2. Dataset Pipeline

## Step 1 — Data Cleaning

- Remove duplicates
- Handle missing latitude & longitude
- Standardize crime names
- Normalize timestamps
- Remove invalid records
- Validate coordinates

## Step 2 — Feature Engineering

Create derived features such as:

- Hour
- Weekday
- Month
- Season
- Weekend
- Time Bucket
- Severity Score
- Cluster ID
- Risk Score

# 3. PostgreSQL Database

Use PostgreSQL for operational data.

## Core Tables

### Users

```
id
name
email
password
role
district
station
created_at
```

### CrimeCases

```
case_id
crime_number
crime_type
description
crime_date
crime_time
district
police_station
latitude
longitude
status
severity
risk_score
created_at
```

### Victims

```
victim_id
case_id
name
age
gender
occupation
```

### Accused

```
accused_id
case_id
name
age
gender
repeat_offender
risk_score
```

### Police Stations

```
station_id
district
name
latitude
longitude
```

### Predictions

```
prediction_id
district
crime_type
prediction
confidence
reason
created_at
```

### Alerts

```
alert_id
district
severity
message
created_at
```

# 4. Neo4j Graph

Use Neo4j for relationship intelligence.

## Nodes

- Person
- Victim
- Accused
- Case
- Vehicle
- Phone
- Weapon
- Location
- PoliceStation

## Relationships

- INVOLVED_IN
- PART_OF
- USED
- VISITED
- OCCURRED_AT
- ASSOCIATED_WITH

# 5. AI Pipeline

Create a separate machine-learning service.

# 6. Machine Learning Models

- Hotspot Prediction: XGBoost
- Clustering: DBSCAN
- Trend Forecasting: ARIMA or Prophet
- Crime Classification: Random Forest
- Anomaly Detection: Isolation Forest
- Explainability: SHAP

# 7. Explainable AI

Every prediction should provide:

- risk
- reason
- confidence
- historical trend
- recommended action

# 8. Recommendation Engine

Actions such as:

- increase patrols
- deploy cameras
- monitor parking lots
- increase surveillance during high-risk hours
