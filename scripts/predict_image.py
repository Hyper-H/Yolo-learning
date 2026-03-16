import argparse

from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run YOLOv8 inference on an image or video.")
    parser.add_argument("--model", default="yolov8n.pt", help="Pretrained model path or model name.")
    parser.add_argument("--source", required=True, help="Path to an image, directory, or video.")
    parser.add_argument("--project", default="results", help="Output root directory.")
    parser.add_argument("--name", default="predict", help="Run name under the output root.")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = YOLO(args.model)
    model.predict(
        source=args.source,
        conf=args.conf,
        project=args.project,
        name=args.name,
        save=True,
    )
    print(f"Saved prediction outputs to {args.project}/{args.name}")


if __name__ == "__main__":
    main()

