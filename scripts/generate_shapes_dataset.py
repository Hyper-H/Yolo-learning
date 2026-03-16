import math
import random
from pathlib import Path


IMG_SIZE = 256
BACKGROUND = (255, 255, 255)
COLORS = {
    "square": (220, 60, 60),
    "circle": (60, 120, 220),
    "triangle": (60, 180, 90),
}
CLASS_TO_ID = {"square": 0, "circle": 1, "triangle": 2}


def point_in_triangle(px: int, py: int, a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    denominator = ((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1]))
    if denominator == 0:
        return False
    w1 = ((b[1] - c[1]) * (px - c[0]) + (c[0] - b[0]) * (py - c[1])) / denominator
    w2 = ((c[1] - a[1]) * (px - c[0]) + (a[0] - c[0]) * (py - c[1])) / denominator
    w3 = 1 - w1 - w2
    return w1 >= 0 and w2 >= 0 and w3 >= 0


def save_ppm(path: Path, pixels: list[tuple[int, int, int]]) -> None:
    with path.open("wb") as f:
        f.write(f"P6\n{IMG_SIZE} {IMG_SIZE}\n255\n".encode("ascii"))
        f.write(bytearray(channel for pixel in pixels for channel in pixel))


def draw_shape(shape: str, seed: int) -> tuple[list[tuple[int, int, int]], tuple[int, int, int, int]]:
    random.seed(seed)
    pixels = [BACKGROUND for _ in range(IMG_SIZE * IMG_SIZE)]
    size = random.randint(72, 120)
    min_x = random.randint(20, IMG_SIZE - size - 20)
    min_y = random.randint(20, IMG_SIZE - size - 20)
    max_x = min_x + size
    max_y = min_y + size
    color = COLORS[shape]

    if shape == "square":
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                pixels[y * IMG_SIZE + x] = color

    elif shape == "circle":
        cx = (min_x + max_x) // 2
        cy = (min_y + max_y) // 2
        radius = size // 2
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                if (x - cx) ** 2 + (y - cy) ** 2 <= radius ** 2:
                    pixels[y * IMG_SIZE + x] = color

    elif shape == "triangle":
        ax = (min_x + max_x) // 2
        ay = min_y
        bx = min_x
        by = max_y
        cx = max_x
        cy = max_y
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                if point_in_triangle(x, y, (ax, ay), (bx, by), (cx, cy)):
                    pixels[y * IMG_SIZE + x] = color
    else:
        raise ValueError(f"Unsupported shape: {shape}")

    return pixels, (min_x, min_y, max_x, max_y)


def yolo_label(shape: str, box: tuple[int, int, int, int]) -> str:
    min_x, min_y, max_x, max_y = box
    x_center = ((min_x + max_x) / 2) / IMG_SIZE
    y_center = ((min_y + max_y) / 2) / IMG_SIZE
    width = (max_x - min_x) / IMG_SIZE
    height = (max_y - min_y) / IMG_SIZE
    return f"{CLASS_TO_ID[shape]} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"


def generate_split(root: Path, split: str, count: int, seed_offset: int) -> None:
    image_dir = root / "images" / split
    label_dir = root / "labels" / split
    image_dir.mkdir(parents=True, exist_ok=True)
    label_dir.mkdir(parents=True, exist_ok=True)

    shapes = list(CLASS_TO_ID)
    for idx in range(count):
        shape = shapes[idx % len(shapes)]
        pixels, box = draw_shape(shape, seed_offset + idx)
        image_path = image_dir / f"{split}_{idx:02d}.ppm"
        label_path = label_dir / f"{split}_{idx:02d}.txt"
        save_ppm(image_path, pixels)
        label_path.write_text(yolo_label(shape, box), encoding="ascii")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    dataset_root = repo_root / "data" / "shapes-mini"
    generate_split(dataset_root, "train", count=18, seed_offset=100)
    generate_split(dataset_root, "val", count=6, seed_offset=1000)
    print(f"Generated dataset at {dataset_root}")


if __name__ == "__main__":
    main()

