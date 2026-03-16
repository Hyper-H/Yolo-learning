# YOLOv8 Usage Notes

## 1. Why Start With YOLOv8

YOLOv8 is a practical starting point because:

- its API is simple
- pretrained weights are easy to use
- training and inference are straightforward
- it is widely used in tutorials and projects

## 2. Typical Workflow

### Inference

Use a pretrained model to detect objects in images or videos.

Example:

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("image.jpg")
```

### Validation

Evaluate a model on a validation dataset.

Typical metrics:

- Precision
- Recall
- mAP50
- mAP50-95

### Training

Train or fine-tune on a dataset defined by a YAML file.

Example dataset YAML usually contains:

- train path
- val path
- number of classes
- class names

## 3. YOLOv8 Model Sizes

Common pretrained models:

- `yolov8n.pt`: nano, fastest, lightest
- `yolov8s.pt`: small
- `yolov8m.pt`: medium
- `yolov8l.pt`: large
- `yolov8x.pt`: extra large, strongest but heavier

For learning and interview demos, start with:

- `yolov8n.pt`

## 4. Important Training Arguments

Typical arguments:

- `epochs`
- `imgsz`
- `batch`
- `device`
- `workers`
- `project`
- `name`

What they mean:

- `epochs`: how many passes over the dataset
- `imgsz`: input image size
- `batch`: number of samples per update
- `device`: cpu or gpu id
- `project/name`: output directory for results

## 5. Common Practical Issues

### Overfitting

Symptoms:

- training metrics improve a lot
- validation metrics do not

Fixes:

- more data
- stronger augmentation
- smaller model
- early stopping

### Small object detection

Fixes:

- larger image size
- higher-quality annotations
- better data collection

### Class imbalance

Fixes:

- more balanced data
- targeted augmentation
- class-aware sampling strategies

## 6. What To Mention In An Interview

Useful points:

- YOLOv8 is anchor-free
- it is strong for practical deployment
- inference speed and model size matter in real applications
- good data matters as much as architecture

