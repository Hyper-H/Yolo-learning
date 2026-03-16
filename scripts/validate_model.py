import argparse

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate a YOLOv8 model.")
    parser.add_argument("--model", default="yolov8n.pt", help="Model weights.")
    parser.add_argument("--data", required=True, help="Dataset YAML path.")
    parser.add_argument("--imgsz", type=int, default=640, help="Input image size.")
    parser.add_argument("--batch", type=int, default=16, help="Batch size.")
    parser.add_argument("--device", default="cpu", help="Device, e.g. cpu, 0.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.model)
    metrics = model.val(
        data=args.data,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
    )
    print(metrics)


if __name__ == "__main__":
    main()

