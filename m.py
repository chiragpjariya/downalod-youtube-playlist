import yt_dlp
import os

# The URL of the YouTube playlist
playlist_url = 'https:/'

# Define the directory where videos will be saved
download_directory = r' '

# Ensure the directory exists
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Options for yt-dlp
ydl_opts = {
    'format': 'best',  # Download best quality without merging
    'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),
}

# Download playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

