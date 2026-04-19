# Design Choices

## 1. YOLOv8 for Detection
YOLOv8 was chosen because:
- It provides high accuracy
- Works well in real-time scenarios
- Easy integration using Ultralytics API

---

## 2. Line Crossing Logic
Instead of complex behavior models:
- A simple horizontal line is used
- Crossing direction determines ENTRY or EXIT
- This reduces computation cost and complexity

---

## 3. JSONL Storage Format
JSONL (JSON Lines) was chosen because:
- Efficient for streaming large data
- Easy to append events
- Works well with real-time systems

---

## 4. FastAPI Backend
FastAPI was selected because:
- High performance
- Easy API development
- Built-in documentation support

---

## 5. Modular Architecture
Code is separated into:
- pipeline/
- app/
- tests/
- docs/

This improves scalability and maintainability.
