# 🏬 Store Intelligence System

## 📌 Overview
This system processes CCTV footage to detect customer movement and generate real-time analytics for retail stores. It simulates a production-like pipeline where events are generated from video streams and consumed by a FastAPI backend to compute insights such as visitor counts, conversion rates, funnels, and anomalies.

---

## 🚀 Features
- YOLOv8 person detection
- Entry/Exit tracking
- Event generation (JSONL format)
- FastAPI backend for real-time analytics
- Metrics & funnel analysis
- Heatmap-ready event structure
- Anomaly detection (e.g., dead zones)

---

## 🎥 Demo Videos
👉 Click below to watch full working demo:

https://drive.google.com/drive/folders/1ZsEuXyD-fT6CuNzzlO9SXphI1_fzamyU?usp=drive_link

---

## ⚙️ Run Pipeline
```bash
python pipeline/detect.py
```
## Run API
```bash
uvicorn app.main:app --reload
API will be available at http://127.0.0.1:8000/docs
```
## project structure
```
/store-intelligence/
├── pipeline/
│   ├── detect.py          # Main detection + tracking script
│   ├── tracker.py         # Re-ID / tracking logic
│   ├── emit.py            # Event schema + emission
│   └── run.sh             # Process all videos → events
│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── models.py          # Pydantic schemas
│   ├── ingestion.py       # Event ingestion + deduplication
│   ├── metrics.py         # Metric computations
│   ├── funnel.py          # Funnel logic
│   ├── anomalies.py       # Anomaly detection logic
│   └── health.py          # Health endpoint
│
├── tests/
│   ├── test_pipeline.py
│   ├── test_metrics.py
│   └── test_anomalies.py
│
├── docs/
│   ├── DESIGN.md          # Architecture + AI decisions
│   └── CHOICES.md         # Key design choices
│
├── docker-compose.yml     # Container setup
└── README.md
```
## Run simulator (generate events)
```
python simulator.py
```
##  Run dashboard (live metrics)
```
python dashboard.py
```
## 🌐 Live API (Deployed)

👉 Access the deployed API here:

https://store-intelligence-j9m8.onrender.com

👉 Swagger UI (Test all APIs):

https://store-intelligence-j9m8.onrender.com/docs

## ## 🧪 Sample Test

Use Swagger Docs to test:

POST /add-event

Example:
{
  "store_id": "STORE_001",
  "camera_id": "CAM_1",
  "visitor_id": "V101",
  "event_type": "ENTRY"
}
