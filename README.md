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
