# Spotify to YouTube MP3 Downloader Documentation

## Overview
This project allows users to retrieve their saved Spotify songs and download them in MP3 format using YouTube as the source. The system works by:
1. Authenticating with Spotify to get the user’s saved songs.
2. Extracting song titles and saving them to a CSV file.
3. Searching for these songs on YouTube and downloading them as MP3 files.

## Prerequisites
Before running the application, ensure you have the following installed:
- Python (>=3.7)
- Required Python libraries (installed via `setup.py`)

## Installation
1. Clone or download the repository.
2. Navigate to the project directory and install dependencies by running:
   ```sh
   pip install -e .
   ```
3. Set up your Spotify API credentials:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create an application and obtain `CLIENT_ID` and `CLIENT_SECRET`
   - Add `http://127.0.0.1:5000/authorize` as a Redirect URI
   - Update `Spotify.py` with these credentials.

## Usage
### 1. Authenticate with Spotify
Run the following command to start the authentication server:
```sh
python Spotify.py
```
This will start a Flask web server. Open a browser and visit `http://127.0.0.1:5000/` to log in to Spotify.

### 2. Retrieve Songs from Spotify
Once logged in, the script will fetch all saved songs and store them in `songs.csv`.

### 3. Download MP3 Files
Run the following command to start downloading:
```sh
python mp3_downloader.py
```
This script will:
- Read song titles from `songs.csv`
- Search YouTube for matching videos
- Download and convert them into MP3 files
- Store them in `Downloads/songs/`

## File Descriptions
### Spotify.py
Handles Spotify authentication and retrieves saved tracks, saving them into a CSV file.
### mp3_downloader.py
Reads `songs.csv`, searches for the songs on YouTube, and downloads them as MP3 files.
### setup.py
Defines dependencies and facilitates package installation. Now includes FFmpeg in the requirements list.

## Notes
- Ensure that FFmpeg is properly installed and accessible in your system’s PATH.
- The accuracy of song downloads depends on YouTube search results.
- If an error occurs, check that your Spotify credentials and dependencies are correctly set up.

## License
MIT License.

## Author
Zeyad Bassyouni

