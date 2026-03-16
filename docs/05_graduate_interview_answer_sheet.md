# Graduate Interview Answer Sheet

## 1. What is YOLO in one sentence?

YOLO is a one-stage object detection framework that predicts object categories and bounding boxes in a single forward pass, which makes it suitable for real-time vision tasks.

## 2. How should you introduce YOLO in an interview?

You can answer like this:

> YOLO is a representative one-stage detector. Its main advantage is speed because it performs localization and classification together instead of using a separate proposal stage. In practice, YOLO is useful when we care about both detection accuracy and real-time performance.

## 3. What is the difference between YOLO and image classification?

Image classification only tells us what is in the image.

YOLO tells us:

- what objects are present
- where they are

## 4. What is the difference between YOLO and Faster R-CNN?

YOLO:

- one-stage
- faster
- easier to deploy in real-time systems

Faster R-CNN:

- two-stage
- often used as a stronger classical accuracy baseline
- slower in practice

## 5. What does the YOLO pipeline look like?

1. input image
2. backbone extracts features
3. neck fuses features from different scales
4. head predicts boxes and classes
5. NMS removes duplicate boxes
6. final results are produced

## 6. What do IoU and NMS mean?

### IoU

IoU measures how much a predicted box overlaps with the ground-truth box.

### NMS

NMS removes repeated overlapping predictions for the same object.

## 7. What is mAP?

mAP means mean Average Precision. It is a common detection metric that summarizes detection quality across classes and overlap thresholds.

## 8. Why is YOLO useful for real projects?

- fast inference
- practical deployment
- easy transfer learning
- strong open-source ecosystem

## 9. What are common difficulties in YOLO projects?

- poor annotation quality
- class imbalance
- small object detection
- domain shift between training and test scenes

## 10. If asked “How would you prepare a YOLO project?”, answer with this structure:

1. define the problem and classes
2. collect and annotate images
3. split train/validation/test
4. fine-tune a pretrained model
5. evaluate with precision, recall, and mAP
6. optimize for deployment speed and robustness

## 11. Good answer for “Why did you study YOLO?”

> I studied YOLO because it is a practical bridge between deep learning theory and deployable computer vision systems. It helped me understand not only model architecture, but also data preparation, training, validation, and inference in a real workflow.

## 12. Good answer for “What have you actually done with YOLO?”

> I built a small YOLOv8 learning project, organized the training and inference scripts, and prepared a miniature dataset to understand the complete detection workflow from data format to evaluation.

## 13. What should you absolutely avoid in an interview?

- only memorizing buzzwords
- confusing classification and detection
- saying mAP is just “accuracy”
- failing to explain NMS, IoU, and the data pipeline

## 14. What should you emphasize?

- clear pipeline understanding
- speed vs accuracy tradeoff
- practical engineering workflow
- data quality and evaluation awareness

