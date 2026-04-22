import subprocess
from processor.ocr import extract_text_from_image

def process_video(video_path):

    frame_path = "last_frame.jpg"

    # extract last frame
    subprocess.call([
        "ffmpeg",
        "-sseof", "-1",
        "-i", video_path,
        "-update", "1",
        "-q:v", "1",
        frame_path
    ])

    # OCR on frame
    return extract_text_from_image(frame_path)