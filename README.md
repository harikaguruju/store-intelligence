# Store Intelligence System

## Overview
This system processes CCTV footage to detect customer movement and generate analytics.

---

## Features
- YOLOv8 person detection
- Entry/Exit tracking
- Event generation (JSONL)
- FastAPI backend
- Metrics & funnel analysis
- Anomaly detection

---

## Run Pipeline
python pipeline/detect.py

---

## Run API
uvicorn app.main:app --reload

---

## Run with Docker
docker-compose up --build

---

## API Endpoints
- /events
- /metrics
- /funnel

---

## Project Structure
/store-intelligence/
├── pipeline/
│   ├── detect.py          # Main detection + tracking script
│   ├── tracker.py         # Re-ID / tracking logic
│   ├── emit.py            # Event schema + emission
│   └── run.sh             # One command to process all clips → events
│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── models.py          # Pydantic event schema
│   ├── ingestion.py       # Ingest, dedup
│   ├── metrics.py         # Real-time metric computation
│   ├── funnel.py          # Funnel + session logic
│   ├── anomalies.py       # Anomaly detection
│   └── health.py
│
├── tests/
│   ├── test_pipeline.py   # Include prompt block header
│   ├── test_metrics.py
│   └── test_anomalies.py
│
├── docs/
│   ├── DESIGN.md          # Architecture + AI-assisted decisions
│   └── CHOICES.md         # 3 decisions with full reasoning
│
├── docker-compose.yml
└── README.md
