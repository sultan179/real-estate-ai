"""
main.py

Main entry point for the
real-estate image pipeline.
"""

from app.ingestion.raw_loader import (
    load_raw_images,
    print_image_info,
)

from app.export.save_preview import (
    save_preview_image,
)


def main():

    # Input RAW image
    raw_path = "data/input/IMG_9735.CR2"

    # Output preview JPG
    output_path = "data/output/preview.jpg"

    # Load RAW image
    image = load_raw_images(raw_path)

    # Print diagnostics
    print_image_info(image)

    # Save preview image
    save_preview_image(image, output_path)


if __name__ == "__main__":
    main()