import subprocess
from tkinter import filedialog, messagebox
from audio_tracks import get_audio_tracks


def delete_selected_audio(file_path, track_vars):
    # Get selected track indexes
    selected_tracks = [idx for idx, var in track_vars if var.get() == 1]

    if not selected_tracks:
        messagebox.showwarning(
            "No Selection",
            "Please select at least one track to delete."
        )
        return

    # Ask where to save the new video
    save_path = filedialog.asksaveasfilename(
        title="Save video as",
        defaultextension=".mp4",
        filetypes=[("MP4 Video", "*.mp4"), ("MKV Video", "*.mkv")]
    )

    if not save_path:
        return

    # Get audio tracks info
    tracks = get_audio_tracks(file_path)
    total_tracks = len(tracks)

    # Always keep video
    map_options = ["-map", "0:v:0"]

    # Keep only unselected audio tracks
    for i in range(total_tracks):
        if i not in selected_tracks:
            map_options += ["-map", f"0:a:{i}"]

    # FFmpeg command
    ffmpeg_cmd = [
        "ffmpeg", "-i", file_path,
        *map_options,
        "-c", "copy",
        save_path
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        messagebox.showinfo(
            "Success",
            f"Video saved successfully:\n{save_path}"
        )
    except subprocess.CalledProcessError as e:
        messagebox.showerror(
            "Error",
            f"Failed to remove audio tracks:\n{e}"
        )