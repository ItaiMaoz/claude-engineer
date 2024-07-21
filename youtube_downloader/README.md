# YouTube Downloader

## Project Overview
This project is a simple YouTube video downloader application that allows users to download videos from YouTube by providing a URL. It offers a command-line interface for easy interaction.

## File Structure
- `youtube_downloader.py`: The main script containing the download functionality.
- `requirements.txt`: Lists the project dependencies.
- `README.md`: This file, providing an overview of the project.

## Key Features
- Downloads YouTube videos at the highest available resolution.
- Allows users to specify a custom download path.
- Displays real-time download progress.
- Implements error handling and logging for better debugging.

## Dependencies
The project currently has a discrepancy in its dependencies:
- The main script (`youtube_downloader.py`) uses the `pytube` library.
- The `requirements.txt` file lists `yt-dlp==2023.12.30` as a dependency.

This discrepancy needs to be resolved for proper functionality.

## Usage
1. Run the script: `python youtube_downloader.py`
2. Enter the YouTube video URL when prompted.
3. Optionally, specify a custom download path or press Enter to use the current directory.

## Notes
- The script uses Python's logging module for comprehensive logging.
- It captures and logs exceptions that may occur during the download process.
- The script prints the Python version for debugging purposes.
- It waits for user input before exiting, which is useful for viewing results in some environments.

## Future Improvements
- Resolve the dependency discrepancy between `pytube` and `yt-dlp`.
- Add more features such as playlist downloading or format selection.
- Improve error handling and user feedback.
- Consider adding a graphical user interface (GUI) for easier use.