"""
Add TadReamk branding (logo + "TadReamk.com") to the top-right of an image.

Usage:
    source venv/bin/activate
    python scripts/add_branding.py --image data/articles/<slug>/diagram.png

Options:
    --padding 20       Padding from edges (default: 20)
    --font-size 28     Font size for "TadReamk.com" (default: 28)
"""

import argparse
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


LOGO_PATH = Path(__file__).parent.parent / "slides" / "public" / "tadreamk_logo.png"


def add_branding(image_path, padding=20, font_size=28):
    img = Image.open(image_path).convert("RGBA")

    if not LOGO_PATH.exists():
        print(f"  Warning: logo not found at {LOGO_PATH}, adding text only")
        logo = None
    else:
        logo = Image.open(LOGO_PATH).convert("RGBA")
        # Scale logo to match font size (roughly 1.5x font height)
        logo_height = int(font_size * 1.5)
        logo_width = int(logo.width * logo_height / logo.height)
        logo = logo.resize((logo_width, logo_height), Image.LANCZOS)

    # Try to load a nice font, fall back to default
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except (OSError, IOError):
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except (OSError, IOError):
            font = ImageFont.load_default()

    text = "TadReamk.com"
    draw = ImageDraw.Draw(img)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    gap = 10  # gap between logo and text
    logo_width = logo.width if logo else 0
    total_width = logo_width + gap + text_width if logo else text_width
    block_height = max(logo.height if logo else 0, text_height)

    # Position: top-right with padding
    x_start = img.width - total_width - padding
    y_start = padding

    # Paste logo
    if logo:
        logo_y = y_start + (block_height - logo.height) // 2
        img.paste(logo, (x_start, logo_y), logo)

    # Draw text
    text_x = x_start + (logo_width + gap if logo else 0)
    text_y = y_start + (block_height - text_height) // 2

    # Draw text with slight shadow for readability on any background
    shadow_color = (0, 0, 0, 80)
    text_color = (100, 100, 100, 200)

    # Detect if background is dark or light at text position
    sample_x = min(text_x + text_width // 2, img.width - 1)
    sample_y = min(text_y + text_height // 2, img.height - 1)
    bg_pixel = img.getpixel((sample_x, sample_y))
    bg_brightness = (bg_pixel[0] * 299 + bg_pixel[1] * 587 + bg_pixel[2] * 114) / 1000

    if bg_brightness < 128:
        # Dark background: light text
        text_color = (200, 200, 200, 200)
        shadow_color = (0, 0, 0, 120)
    else:
        # Light background: dark text
        text_color = (100, 100, 100, 220)
        shadow_color = (255, 255, 255, 80)

    draw.text((text_x + 1, text_y + 1), text, font=font, fill=shadow_color)
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    # Save as RGB (PNG)
    img = img.convert("RGB")
    img.save(image_path)

    print(f"  Branding added to {image_path}")


def main():
    parser = argparse.ArgumentParser(description="Add TadReamk branding to an image")
    parser.add_argument("--image", required=True, help="Path to image to brand")
    parser.add_argument("--padding", type=int, default=20, help="Padding from edges (default: 20)")
    parser.add_argument("--font-size", type=int, default=28, help="Font size (default: 28)")
    args = parser.parse_args()

    if not Path(args.image).exists():
        print(f"Error: {args.image} not found")
        sys.exit(1)

    add_branding(args.image, padding=args.padding, font_size=args.font_size)
    print("Done!")


if __name__ == "__main__":
    main()
