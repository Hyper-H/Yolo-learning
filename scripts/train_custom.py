import argparse

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train or fine-tune a YOLOv8 model.")
    parser.add_argument("--model", default="yolov8n.pt", help="Starting model weights.")
    parser.add_argument("--data", required=True, help="Dataset YAML path.")
    parser.add_argument("--epochs", type=int, default=50, help="Training epochs.")
    parser.add_argument("--imgsz", type=int, default=640, help="Input image size.")
    parser.add_argument("--batch", type=int, default=16, help="Batch size.")
    parser.add_argument("--device", default="cpu", help="Device, e.g. cpu, 0, 0,1.")
    parser.add_argument("--project", default="results", help="Output root directory.")
    parser.add_argument("--name", default="train", help="Run name.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.model)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
        project=args.project,
        name=args.name,
    )
    print(f"Training artifacts saved to {args.project}/{args.name}")


if __name__ == "__main__":
    main()

