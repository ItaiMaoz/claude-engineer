import os
from pytube import YouTube
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"\rDownload progress: {percentage_of_completion:.2f}%", end="")

def download_video(url, output_path='.'):
    logging.info(f"Starting download process for URL: {url}")
    logging.info(f"Output path: {output_path}")

    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        logging.info(f"Video title: {yt.title}")
        
        # Get the highest resolution stream
        video = yt.streams.get_highest_resolution()
        
        logging.info(f"Downloading video: {video.title}")
        video.download(output_path)
        
        logging.info(f"Download complete! Saved to: {output_path}")
        return True
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        logging.error("Error details:", exc_info=True)
        return False

if __name__ == "__main__":
    logging.info("Script started")
    video_url = input("Enter the YouTube video URL: ")
    logging.info(f"User entered URL: {video_url}")

    download_path = input("Enter the download path (press Enter for current directory): ")
    logging.info(f"User entered download path: {download_path}")
    
    if not download_path:
        download_path = '.'
    
    if not os.path.exists(download_path):
        logging.info(f"Creating directory: {download_path}")
        os.makedirs(download_path)
    
    logging.info("Calling download_video function")
    success = download_video(video_url, download_path)
    
    if not success:
        logging.error("Download failed. Please check the URL and try again.")
    else:
        logging.info("Download process completed successfully")
    
    # Print Python version for debugging
    logging.info(f"Python version: {sys.version}")

    logging.info("Script finished")
    
    input("Press Enter to exit...")