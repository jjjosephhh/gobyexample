import os
from pathlib import Path
import shutil
from pdf2image import convert_from_path


def pdf_to_images(src_path, dest_dir):
    if os.path.exists(dest_dir) and os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    images = convert_from_path(src_path)
    for i, im in enumerate(images):
        path = os.path.join(dest_dir, f"{i:03}.webp")
        im.save(path, format="webp", optimize=True, quality=100)


if __name__ == "__main__":
    zines = [
        (
            os.path.join("zines", "tcpdump-zine.pdf"),
            os.path.join("docs", "zines-staging", "tcpdump"),
        ),
        (
            os.path.join("zines", "debugging-zine.pdf"),
            os.path.join("docs", "zines-staging", "debugging"),
        ),
        (
            os.path.join("zines", "networking-zine.pdf"),
            os.path.join("docs", "zines-staging", "networking"),
        ),
        (
            os.path.join("zines", "perf-zine.pdf"),
            os.path.join("docs", "zines-staging", "perf"),
        ),
        (
            os.path.join("zines", "wizard-zine.pdf"),
            os.path.join("docs", "zines-staging", "wizard"),
        ),
        (
            os.path.join("zines", "strace-zine-v3.pdf"),
            os.path.join("docs", "zines-staging", "strace"),
        ),
    ]
    for src_path, dest_dir in zines:
        pdf_to_images(src_path, dest_dir)
