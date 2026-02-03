import tkinter as tk
from tkinter import filedialog, messagebox
from audio_tracks import get_audio_tracks
from delete_audio import delete_selected_audio

def create_button(parent):
    track_vars = []  # To store checkbox variables
    def select_video():
        file_path = filedialog.askopenfilename(
            title="Select video file",
            filetypes=[("Video Files", "*.mp4 *.mkv *.mov")]
        )
        if file_path:
            print("Selected video:", file_path)

            # Clear previous checkboxes/buttons
            for widget in parent.winfo_children():
                widget.destroy()
            track_vars.clear()

            # Get audio tracks
            tracks = get_audio_tracks(file_path)

            # Create checkboxes for each audio track
            for idx, track in enumerate(tracks):
                var = tk.IntVar()
                chk = tk.Checkbutton(parent, text=f"Track {idx+1}: {track}", variable=var)
                chk.pack(pady=2)
                track_vars.append((idx, var))

            # Instruction label
            info_label = tk.Label(
                parent,
                text="Select the audio tracks you want to delete and click the button below",
                fg="gray"
            )
            info_label.pack(pady=10)

            # Delete Selected Tracks button
            delete_btn = tk.Button(
                parent,
                text="Delete Selected Tracks",
                command=lambda: delete_selected_audio(file_path,track_vars)
            )
            delete_btn.pack(pady=10)

    # Upload video button
    button = tk.Button(parent, text="Upload Video", command=select_video)
    button.pack(pady=50)
    return button