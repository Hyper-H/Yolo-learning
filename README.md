# YOLO Learning

A practical YOLOv8 learning project for:

- understanding the main principles of YOLO
- learning how to run training, validation, and inference
- preparing for graduate school interviews with a clear set of notes

## Why This Repo Exists

This repository is designed as a study workspace, not just a code dump. It combines:

- conceptual notes
- interview-oriented summaries
- runnable YOLOv8 scripts
- a clean folder structure for future experiments

## Recommended Learning Path

1. Read [docs/01_yolo_fundamentals.md](docs/01_yolo_fundamentals.md)
2. Read [docs/02_yolov8_usage.md](docs/02_yolov8_usage.md)
3. Read [docs/03_interview_qa.md](docs/03_interview_qa.md)
4. Follow [docs/04_study_roadmap.md](docs/04_study_roadmap.md)
5. Read [docs/05_graduate_interview_answer_sheet.md](docs/05_graduate_interview_answer_sheet.md)
6. Read [docs/06_quick_start_with_mini_dataset.md](docs/06_quick_start_with_mini_dataset.md)
7. Run the scripts in `scripts/`

## Project Structure

```text
.
├── docs/
├── scripts/
├── data/
│   └── shapes-mini/
├── models/
├── experiments/
├── requirements.txt
└── README.md
```

## Environment Setup

Use Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Quick Start

### 1. Check environment

```bash
py -3 scripts/check_env.py
```

### 2. Run inference with a pretrained model

```bash
py -3 scripts/predict_image.py --source path/to/image.jpg
```

### 3. Validate a pretrained model

```bash
py -3 scripts/validate_model.py --model yolov8n.pt --data coco8.yaml
```

### 4. Train on a custom dataset

```bash
py -3 scripts/train_custom.py --data path/to/data.yaml
```

### 5. Train immediately on the built-in mini dataset

```bash
py -3 scripts/train_shapes_demo.py
```

## What You Should Be Able To Explain In An Interview

After working through this repo, you should be able to explain:

- what object detection is and why YOLO is fast
- the difference between one-stage and two-stage detectors
- how YOLO predicts bounding boxes and classes
- the role of NMS, IoU, confidence score, and mAP
- why YOLOv8 is anchor-free and why that matters
- how to fine-tune YOLO on a custom dataset
- how to explain a small end-to-end YOLO project in an interview

## Practical Advice For Interview Prep

- Do not only memorize model names.
- Be ready to explain the full pipeline:
  image -> backbone -> neck -> detection head -> NMS -> final boxes
- Be ready to compare YOLO with Faster R-CNN and SSD.
- Be ready to explain one real project idea using YOLO.
