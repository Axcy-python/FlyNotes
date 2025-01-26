from PIL import Image
from pathlib import Path


def compress_image(image_path: Path, output_path: Path, size: tuple[int, int] = (60, 60)) -> None:
    try:
        with Image.open(image_path) as img:
            img = img.resize(size)
            img.save(output_path, optimize=True, quality=85)
            print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

