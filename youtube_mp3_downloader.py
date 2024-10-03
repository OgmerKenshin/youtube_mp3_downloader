import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def download_youtube_audio(youtube_url, output_dir="downloads"):
    """
    Downloads the audio from the YouTube video at the specified URL and converts it to MP3 format.
    """

    # Print the URL to verify what’s being passed
    print(f"Downloading from URL: {youtube_url}")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Set up yt-dlp options to download the best quality audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Save the file as title.extension
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # You can set the audio quality here
        }],
        "ffmpeg_location": r"c:\ffmpeg-2024-09-26-git-f43916e217-full_build\bin" # Path to your ffmpeg installation
    }