# Interview Q&A Cheat Sheet

## Q1. What is the difference between image classification and object detection?

Classification predicts what is in the image.

Detection predicts:

- what objects are present
- where they are located

## Q2. Why is YOLO called a one-stage detector?

Because it directly predicts boxes and classes in a single pass, without a separate region proposal stage.

## Q3. Why is YOLO fast?

- single forward pass
- no separate proposal network
- efficient backbone/neck/head design

## Q4. What is NMS?

Non-Maximum Suppression removes overlapping duplicate predictions and keeps the best box.

## Q5. What is IoU?

Intersection over Union is the overlap ratio between predicted and ground-truth boxes.

## Q6. What is mAP?

Mean Average Precision summarizes detection performance across classes and IoU thresholds.

## Q7. What does anchor-free mean in YOLOv8?

It means the model does not rely on predefined anchor boxes in the traditional way. This simplifies the detection head and can improve flexibility.

## Q8. YOLO vs Faster R-CNN?

YOLO:

- faster
- simpler deployment
- strong for real-time tasks

Faster R-CNN:

- often used as a stronger accuracy baseline
- generally slower

## Q9. What matters most in a real detection project?

- dataset quality
- annotation quality
- class definition clarity
- deployment constraints
- speed/accuracy tradeoff

## Q10. If asked “How would you use YOLO in a project?”, what should you say?

Give a practical pipeline:

1. define the business problem
2. collect and annotate data
3. split train/val/test
4. fine-tune a pretrained YOLO model
5. evaluate with mAP, precision, recall
6. optimize for inference speed and deployment

## Strong Short Self-Introduction Angle

You can say:

> I studied YOLO as a practical object detection framework because it connects deep learning theory with deployable computer vision systems. I focused on both the architecture and the real workflow of fine-tuning, validating, and running inference.

