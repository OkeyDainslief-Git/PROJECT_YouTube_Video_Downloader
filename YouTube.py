import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path, mode, quality):
    try:
        if mode == "audio":
            format_option = "bestaudio"
        else:
            if quality == "720p":
                format_option = "bestvideo[height<=720]+bestaudio/best"
            elif quality == "480p":
                format_option = "bestvideo[height<=480]+bestaudio/best"
            else:
                format_option = "bestvideo+bestaudio/best"

        yd1_opts = {
            "format": format_option,
            "outtmpl": f"{save_path}/%(title)s_%(id)s.%(ext)s",
            "writethumbnail": True,

                "postprocessors": [
                    {"key": "FFmpegMetadata"},
                    {"key": "EmbedThumbnail"}
                ]
        }
      

        with yt_dlp.YoutubeDL(yd1_opts) as ydl:
            ydl.download([url])

        print("Download completed successfully.")


    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    
    return folder
    
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    video_url = input("Enter the YouTube video URL: ")

    mode = input("Enter download mode (audio/video): ").lower()
    quality = input("Enter video quality (720p/480p/best): ").lower()

    save_dir = open_file_dialog()
     
    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir, mode, quality)
    else:
        print("Invalid save location. ")






