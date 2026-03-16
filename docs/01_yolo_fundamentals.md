# YOLO Fundamentals

## 1. What YOLO Solves

YOLO stands for **You Only Look Once**. It is an object detection model that predicts:

- where objects are
- what classes they belong to

in a single forward pass.

That is why YOLO is known for speed.

## 2. Why YOLO Matters

Traditional detection pipelines often separate region proposal and classification. YOLO treats detection as a direct regression/classification problem, which makes it fast enough for near real-time tasks.

Common application areas:

- surveillance
- autonomous driving
- industrial inspection
- retail counting
- robotics

## 3. One-Stage vs Two-Stage Detection

### Two-stage detectors

Examples:

- R-CNN
- Fast R-CNN
- Faster R-CNN

Process:

1. propose candidate regions
2. classify/refine each region

Advantage:

- often strong accuracy

Disadvantage:

- slower

### One-stage detectors

Examples:

- YOLO
- SSD
- RetinaNet

Process:

1. directly predict boxes and classes over the image

Advantage:

- fast

Disadvantage:

- historically had more difficulty with small objects, though newer versions improved a lot

## 4. Core Detection Concepts

### Bounding box

A rectangle around an object.

Usually represented by:

- center x
- center y
- width
- height

or by corner coordinates.

### Confidence score

How sure the model is that an object exists in the predicted box.

### Class probability

How likely the object belongs to each class.

### IoU

Intersection over Union measures overlap between predicted box and ground-truth box.

Formula:

```text
IoU = overlap area / union area
```

### NMS

Non-Maximum Suppression removes duplicated boxes that point to the same object.

## 5. Typical YOLO Pipeline

1. Input image is resized and normalized
2. Backbone extracts features
3. Neck fuses multi-scale features
4. Detection head predicts boxes, objectness/confidence, and classes
5. NMS filters duplicate boxes
6. Final detection results are returned

## 6. How YOLO Evolved

### Early YOLO versions

- focused on speed
- grid-based prediction
- anchor boxes used in later generations

### YOLOv5 / YOLOv7 / YOLOv8 era

- more engineering improvements
- better training pipeline
- stronger data augmentation
- better multi-scale detection

### YOLOv8

Key traits:

- anchor-free design
- improved training/inference workflow in Ultralytics
- easy-to-use Python API and CLI

## 7. Interview-Level Summary

If an interviewer asks “What is YOLO?”, a good short answer is:

> YOLO is a one-stage object detection model that directly predicts object categories and bounding boxes in one forward pass, which makes it fast and suitable for real-time applications.

