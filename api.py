from youtube_transcript_api import YouTubeTranscriptApi
import os

proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies=proxies)
        return "\n".join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Remove or comment out the following lines
# video_id = "3qHkcs3kG44"  # Replace with your video ID
# transcript = YouTubeTranscriptApi.get_transcript(video_id)
# 
# for entry in transcript:
#     print(entry['text'])