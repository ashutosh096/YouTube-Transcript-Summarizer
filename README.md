YouTube Transcript Summarizer is a web-based tool that extracts the transcript of a YouTube video and generates a concise summary using Natural Language Processing (NLP). The goal of this project is to help users quickly understand the main ideas of long videos without watching the entire content
Features was as follows of this projects, 
Extract transcript from YouTube videos.
Generate short and meaningful summaries.
Simple and clean user interface.
Fast processing of long transcripts.
Saves time for students and researchers.
Tech Stack
Frontend,
HTML
CSS
JavaScript
Backend:
Node.js / Python (depending on implementation)
Libraries / APIs:\
YouTube Transcript API
NLP summarization libraries
How it works 
User enters a YouTube video URL.
The system fetches the transcript of the video.
The transcript text is processed using an NLP summarization algorithm.
The summarized content is displayed to the user.
\\ code
youtube-transcript-summarizer
│
├── app.py
├── requirements.txt
└── templates
      └── index.html
      pip install -r requirements.txt
      from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import re

app = Flask(__name__)

# extract video id from youtube url
def get_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1)

# generate summary from transcript text
def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 5)   # 5 sentences summary
    result = ""
    for sentence in summary:
        result += str(sentence) + " "
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    
    if request.method == "POST":
        url = request.form["url"]
        video_id = get_video_id(url)

        # fetch transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t['text'] for t in transcript])

        # summarize transcript
        summary = summarize_text(text)

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)

    <!DOCTYPE html>
<html>
<head>
<title>YouTube Transcript Summarizer</title>
<style>
body{
font-family:Arial;
background:#f4f4f4;
text-align:center;
margin-top:80px;
}
input{
width:400px;
padding:10px;
}
button{
padding:10px 20px;
margin-left:10px;
}
.summary{
width:60%;
margin:auto;
margin-top:30px;
background:white;
padding:20px;
border-radius:8px;
}
</style>
</head>

<body>

<h2>YouTube Transcript Summarizer</h2>

<form method="POST">
<input type="text" name="url" placeholder="Enter YouTube Video URL" required>
<button type="submit">Summarize</button>
</form>

{% if summary %}
<div class="summary">
<h3>Summary</h3>
<p>{{summary}}</p>
</div>
{% endif %}

</body>
</html>
\\RUNS 
python app.py

How it Works
1️⃣ User enters YouTube URL
2️⃣ YouTube Transcript API extracts transcript
3️⃣ Transcript converted into text
4️⃣ LSA NLP algorithm generates summary
5️⃣ Summary shown on webpage
