import yt_dlp
import os

def download_video(url, output_path='.', audio_only=False):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info)
            print(f"Downloading: {info['title']}")
            ydl.download([url])
            print(f"Download completed: {filename}")
            print(f"Format: {'Audio' if audio_only else 'Video'}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (press Enter for current directory): ").strip()
    audio_only = input("Download audio only? (y/n): ").lower() == 'y'
    
    if not download_path:
        download_path = '.'
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    print("Note: This script will download the best available format without conversion.")
    print("The file format may vary depending on what's available for the video.")
    
    download_video(video_url, download_path, audio_only)

    input("Press Enter to exit...")