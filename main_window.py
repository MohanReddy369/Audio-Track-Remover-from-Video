import tkinter as tk
from upload_video import create_button
from config import FFMPEG_PATH, FFPROBE_PATH
print(FFMPEG_PATH)
print(FFPROBE_PATH)
root=tk.Tk()
root.title("Audio Track Remover")
root.state("zoomed")
create_button(root)
root.mainloop()