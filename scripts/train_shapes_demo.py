from ultralytics import YOLO


def main() -> None:
    model = YOLO("yolov8n.pt")
    model.train(
        data="data/shapes-mini.yaml",
        epochs=20,
        imgsz=256,
        batch=8,
        device="cpu",
        project="results",
        name="shapes_train",
    )
    print("Training complete. Check results/shapes_train for outputs.")


if __name__ == "__main__":
    main()

