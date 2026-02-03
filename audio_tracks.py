import subprocess
import json
from config import FFPROBE_PATH

def get_audio_tracks(video_path):
    cmd = [
        FFPROBE_PATH,
        "-v", "error",
        "-select_streams", "a",
        "-show_entries",
        "stream=index:stream_tags=language,title",
        "-of", "json",
        video_path
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    data = json.loads(result.stdout)

    audio_tracks = []

    for stream in data.get("streams", []):
        index = stream.get("index")

        tags = stream.get("tags", {})
        language = tags.get("language")
        title = tags.get("title")

        # fallback logic
        if language:
            lang = language
        elif title:
            lang = title
        else:
            lang = "unknown"

        audio_tracks.append({
            "index": index,
            "language": lang
        })

    return audio_tracks
