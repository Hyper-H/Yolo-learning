import importlib
import platform
import sys


def module_version(name: str) -> str:
    try:
        module = importlib.import_module(name)
    except Exception as exc:  # pragma: no cover - diagnostic script
        return f"not available ({exc})"
    return getattr(module, "__version__", "installed")


def main() -> None:
    print("Python:", sys.version.replace("\n", " "))
    print("Platform:", platform.platform())
    print("ultralytics:", module_version("ultralytics"))
    print("torch:", module_version("torch"))
    print("cv2:", module_version("cv2"))

    try:
        import torch

        print("CUDA available:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("CUDA device count:", torch.cuda.device_count())
            print("CUDA device 0:", torch.cuda.get_device_name(0))
    except Exception as exc:  # pragma: no cover - diagnostic script
        print("Torch CUDA check skipped:", exc)


if __name__ == "__main__":
    main()

