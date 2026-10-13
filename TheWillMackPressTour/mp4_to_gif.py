
from pathlib import Path
from moviepy import VideoFileClip

# -------- SETTINGS --------
INPUT_FILE = "teaser2.mov"
OUTPUT_FILE = "teaser2.gif"

FPS = 12            # Frames per second
WIDTH = 1322
HEIGHT = 1660         
START_TIME = 0       # Start time in seconds
END_TIME = None      # End time in seconds; None means the end
# --------------------------


def main():
    folder = Path(__file__).resolve().parent
    video_path = folder / INPUT_FILE
    gif_path = folder / OUTPUT_FILE

    if not video_path.exists():
        raise FileNotFoundError(
            f"Video not found: {video_path}\n"
            "Check INPUT_FILE and make sure the video is in this folder."
        )

    with VideoFileClip(str(video_path)) as video:
        end = END_TIME if END_TIME is not None else video.duration
        end = min(end, video.duration)

        if START_TIME < 0 or START_TIME >= end:
            raise ValueError("Please check START_TIME and END_TIME.")

        clip = video.subclipped(START_TIME, end)

        # Resize while preserving the original aspect ratio.
        clip = clip.resized(width=WIDTH)

        # Convert to GIF.
        clip.write_gif(
            str(gif_path),
            fps=FPS,
            logger="bar",
        )

        clip.close()

    print(f"\nGIF saved successfully:\n{gif_path}")


if __name__ == "__main__":
    main()
