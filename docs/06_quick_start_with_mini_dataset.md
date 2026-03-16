# Quick Start With The Mini Dataset

This repo includes a self-contained synthetic dataset so you can start training without downloading external data.

## What is included

- 3 classes: `square`, `circle`, `triangle`
- train/val split already prepared
- YOLO-format labels already generated
- dataset YAML at `data/shapes-mini.yaml`

## Recommended first commands

### 1. Check environment

```bash
py -3 scripts/check_env.py
```

### 2. Train on the mini dataset

```bash
py -3 scripts/train_shapes_demo.py
```

### 3. Validate the trained model

```bash
py -3 scripts/validate_model.py --model results/shapes_train/weights/best.pt --data data/shapes-mini.yaml
```

### 4. Run inference on a sample image from the dataset

```bash
py -3 scripts/predict_image.py --model results/shapes_train/weights/best.pt --source data/shapes-mini/images/val/val_00.ppm
```

## What you should observe

- the result directories under `results/`
- predicted boxes on the validation image
- training metrics such as precision, recall, and mAP

## Why this mini dataset is useful

It is not for serious research accuracy. It is for:

- understanding YOLO data format
- understanding the train/validate/predict workflow
- building confidence before moving to real datasets

