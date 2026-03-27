from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_id(url_or_id):
    if "youtube.com/watch?v=" in url_or_id:
        return url_or_id.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url_or_id:
        return url_or_id.split("youtu.be/")[1].split("?")[0]
    else:
        return url_or_id

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        text = formatter.format_transcript(transcript)
        return text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def summarize_text(text, ratio=0.1):
    sentences = text.split(". ")
    if not sentences:
        return text
    keep = max(1, int(len(sentences) * ratio))
    summary = ". ".join(sentences[:keep])
    return summary + ("..." if keep < len(sentences) else "")

def main():
    print("===== YouTube Transcript Summarizer =====")
    url_or_id = input("Enter YouTube video URL or ID (no playlists!): ").strip()
    video_id = get_video_id(url_or_id)
    print(f"Fetching transcript for video ID: {video_id} ...")

    transcript = fetch_transcript(video_id)
    if not transcript:
        print("Transcript could not be fetched. Exiting.")
        return

    print("\nTranscript fetched successfully!\n")
    summary = summarize_text(transcript)

    print("===== Summary =====")
    print(summary)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("\nSummary saved to summary.txt")

if __name__ == "__main__":
    main()