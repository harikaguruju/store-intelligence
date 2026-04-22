# 🏬 Store Intelligence System

## 📌 Overview
This system processes CCTV footage to detect customer movement and generate real-time analytics for retail stores. It simulates a production-like pipeline where events are generated from video streams and consumed by a FastAPI backend to compute insights such as visitor counts, conversion rates, funnels, and anomalies.

---

## 🚀 Features
- 🎯 YOLOv8-based person detection
- 🚪 Entry & Exit tracking
- 🔄 Event generation (JSONL format)
- ⚡ FastAPI backend for real-time analytics
- 📊 Metrics computation (visitors, conversion rate)
- 🔽 Funnel analysis (entry → exit)
- 📍 Heatmap-ready event structure
- 🚨 Anomaly detection (dead zones, unusual patterns)
- 🐳 Dockerized deployment


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

## 🐳 Docker Setup (Evaluation Requirement)

This project is fully containerized using Docker.
The API can be started with a single command.

---

### 🔧 Prerequisites

* Install Docker Desktop
* Ensure Docker is running

---

### ▶️ Run the Application

```bash
docker compose up --build
```

---

### 🌐 Access the API

After the container starts, open:

```id="a1"
http://localhost:8000/docs
```

👉 This will open Swagger UI where all APIs can be tested.

---

### 🧪 Test the API

1. Open `/docs`
2. Use **POST /add-event**

Example:

```json id="a2"
{
  "store_id": "STORE_001",
  "camera_id": "CAM_1",
  "visitor_id": "V101",
  "event_type": "ENTRY"
}
```

3. Check results in:

* `/metrics`
* `/funnel`

---

### 🛑 Stop the Application

Press:

```bash id="a3"
Ctrl + C
```

---

### 📌 Notes

* No manual setup required
* All dependencies are installed inside the container
* The system is fully reproducible using Docker
* Verified locally using `docker compose up --build`

---


## 🧪 Sample Test

Use Swagger Docs to test:

POST /add-event

Example:
{
  "store_id": "STORE_001",
  "camera_id": "CAM_1",
  "visitor_id": "V101",
  "event_type": "ENTRY"
}
