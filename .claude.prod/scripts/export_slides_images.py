"""
Export slide presentation to a PNG image.

Crops to the #slide-content element's bounding box in the DOM,
so the output is exactly the rendered content with no guesswork.

Usage:
    source venv/bin/activate
    python scripts/export_slides_images.py --url http://localhost:3009

    # Custom output and size:
    python scripts/export_slides_images.py --url http://localhost:3009 --output slides/slide.png --width 1920 --height 1080

    # Custom padding around the content element:
    python scripts/export_slides_images.py --url http://localhost:3009 --padding 30

Requires: playwright (installed in venv)
Install browser if needed: playwright install chromium
"""

import argparse
import sys
import time
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Export slide to PNG image")
    parser.add_argument("--url", required=True, help="URL of the running slide app (e.g. http://localhost:3009)")
    parser.add_argument("--output", default="slides/slide.png", help="Output PNG path (default: slides/slide.png)")
    parser.add_argument("--width", type=int, default=1920, help="Viewport width (default: 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Viewport height (default: 1080)")
    parser.add_argument("--padding", type=int, default=20, help="Padding around content element (default: 20)")
    parser.add_argument("--selector", default="#slide-content", help="CSS selector for the content element (default: #slide-content)")
    args = parser.parse_args()

    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: playwright not installed. Run: pip install playwright && playwright install chromium")
        sys.exit(1)

    print(f"Capturing {args.url} at {args.width}x{args.height}...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": args.width, "height": args.height})
        page.goto(args.url)
        page.wait_for_load_state("networkidle")
        # Wait for React render + Framer Motion animations to complete
        time.sleep(3)

        element = page.query_selector(args.selector)
        if element is None:
            print(f"  Warning: '{args.selector}' not found, falling back to full-page screenshot")
            page.screenshot(path=str(output_path), full_page=False)
        else:
            bbox = element.bounding_box()
            # Expand by padding, clamped to viewport
            clip = {
                "x": max(0, bbox["x"] - args.padding),
                "y": max(0, bbox["y"] - args.padding),
                "width": min(args.width - max(0, bbox["x"] - args.padding), bbox["width"] + args.padding * 2),
                "height": min(args.height - max(0, bbox["y"] - args.padding), bbox["height"] + args.padding * 2),
            }
            page.screenshot(path=str(output_path), clip=clip)
            print(f"  Content box: {bbox['width']:.0f}x{bbox['height']:.0f} at ({bbox['x']:.0f},{bbox['y']:.0f})")
            print(f"  Output: {clip['width']:.0f}x{clip['height']:.0f} (with {args.padding}px padding)")

        browser.close()

    print(f"  Saved: {output_path}")
    print("Done!")


if __name__ == "__main__":
    main()
