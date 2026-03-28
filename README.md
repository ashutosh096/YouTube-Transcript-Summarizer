YouTube Transcript Summarizer

A Python tool to fetch YouTube video transcripts and generate a short summary automatically. Saves the summary to a text file.

Features
Fetch transcript of a single YouTube video by URL or ID.
Summarize the transcript automatically (default: 10% of the sentences).
Save the summary to summary.txt.
Easy to use with a command-line interface.
Requirements
Python 3.12 (highly recommended)
Libraries:
pip install git+https://github.com/jdepoix/youtube-transcript-api.git
Installation
Clone or download this repository to your local machine.
Open terminal or PowerShell and navigate to the project folder:
cd D:\youtube\youtube_transcript_project
Create a virtual environment:
python -m venv .venv
. .\.venv\Scripts\Activate.ps1   # For PowerShell
Install the required library:
pip install --upgrade pip
pip install git+https://github.com/jdepoix/youtube-transcript-api.git
Usage
Run the main script:
python main.py
Enter the YouTube video URL (single video, no playlists). Example:
https://www.youtube.com/watch?v=qsKPEVIgrxU
The script will:
Fetch the transcript for the video.
Generate a summary of the transcript.
Display the summary in the terminal.
Save the summary to summary.txt in the project folder.
Example
===== YouTube Transcript Summarizer =====
Enter YouTube video URL or ID (no playlists!): https://www.youtube.com/watch?v=qsKPEVIgrxU
Fetching transcript for video ID: qsKPEVIgrxU ...

Transcript fetched successfully!

References:
Streamlit: https://docs.streamlit.io/
Google Gemini AI: https://ai.google.dev/
YouTube Transcript API: https://pypi.org/project/youtube-transcript-api/
Langcodes: https://pypi.org/project/langcodes/

===== Summary =====
This is a short summary of the transcript...
Notes
Playlist URLs are not supported; only single video URLs.
Make sure the video has a transcript available; otherwise, the script will return an error.
Recommended to use Python 3.12 with a virtual environment for compatibility

![image alt](https://github.com/ashutosh096/YouTube-Transcript-Summarizer/blob/b6d9c45983cca7a6b9264abc98f21340a0d493ff/youtube_banner.JPG)
![image alt](https://github.com/ashutosh096/YouTube-Transcript-Summarizer/blob/24ce657162226fa8cab2206512c424ade5b72603/Screenshot%202026-03-28%20143913.png)
