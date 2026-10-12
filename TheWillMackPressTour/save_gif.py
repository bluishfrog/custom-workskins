
from pathlib import Path
from io import BytesIO
import asyncio

from PIL import Image
from playwright.async_api import async_playwright


# ---------- SETTINGS ----------
WIDTH = 1280
HEIGHT = 720
FPS = 12
DURATION_SECONDS = 5
OUTPUT_FILE = "teaser_willmack_press_tour.gif"
# ----------------------------


async def main():
    folder = Path(__file__).resolve().parent
    html_file = folder / "youtube_teaser_gif.html"
    output_file = folder / OUTPUT_FILE

    if not html_file.exists():
        raise FileNotFoundError(
            f"Couldn't find {html_file}\n"
            "Put this Python file beside your index.html."
        )

    frames = []
    total_frames = FPS * DURATION_SECONDS
    delay_ms = round(1000 / FPS)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": WIDTH, "height": HEIGHT},
            device_scale_factor=1,
        )

        # Open your actual HTML/CSS page.
        await page.goto(html_file.as_uri(), wait_until="networkidle")

        # Give remote images and fonts a moment to load.
        await page.wait_for_timeout(1500)

        for i in range(total_frames):
            screenshot = await page.screenshot(
                type="png",
                full_page=False,
            )

            frame = Image.open(BytesIO(screenshot)).convert("RGB")
            frames.append(frame)

            # Let CSS animations and progress indicators advance.
            await page.wait_for_timeout(delay_ms)

        await browser.close()

    # GIF supports a limited color palette, so convert each frame.
    gif_frames = [
        frame.convert(
            "P",
            palette=Image.Palette.ADAPTIVE,
            colors=128,
        )
        for frame in frames
    ]

    gif_frames[0].save(
        output_file,
        save_all=True,
        append_images=gif_frames[1:],
        duration=delay_ms,
        loop=0,
        optimize=False,
        disposal=2,
    )

    print(f"GIF saved to: {output_file}")


if __name__ == "__main__":
    asyncio.run(main())
