# System Design

## Overview
The Store Intelligence System processes CCTV footage to detect customer movement and generate real-time analytics.

---

## Architecture

### 1. Pipeline Layer (Computer Vision)
- YOLOv8 is used for person detection
- OpenCV is used for video processing
- Tracking is handled using YOLO tracking (persist=True)
- Entry/Exit is determined using line crossing logic

---

### 2. Event Generation
Each detected movement generates structured events:
- ENTRY
- EXIT

Events are stored in JSONL format for scalability.

---

### 3. Backend Layer (FastAPI)
FastAPI is used to:
- Serve event data
- Compute real-time metrics
- Provide funnel analysis
- Detect anomalies

---

## Data Flow

Video → Detection → Tracking → Event Generation → JSONL → FastAPI → API Response

---

## AI-Assisted Decisions

1. Used YOLOv8 for real-time detection due to high speed and accuracy
2. Used line-crossing logic instead of complex models for simplicity
3. Used JSONL for efficient streaming of large event data
