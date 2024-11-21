from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup
import requests
import re


class GetVideo:
    @staticmethod
    def Id(link):
        """Extracts the video ID from a YouTube video link."""
        if "youtube.com" in link:
            pattern = r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
        elif "youtu.be" in link:
            pattern = r'youtu\.be/([a-zA-Z0-9_-]+)'
        else:
            return None
        match = re.search(pattern, link)
        return match.group(1) if match else None

    @staticmethod
    def title(link):
        """Fetches the title of a YouTube video."""
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            return soup.find("meta", itemprop="name")["content"]
        except TypeError:
            return "⚠️ Invalid YouTube link. Please check the URL."

    @staticmethod
    def transcript(link):
        """Fetches the transcript of a YouTube video."""
        video_id = GetVideo.Id(link)
        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
            return " ".join(item["text"] for item in transcript_data)
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def transcript_time(link):
        """Fetches the transcript with timestamps."""
        video_id = GetVideo.Id(link)
        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
            result = ""
            for item in transcript_data:
                start = int(item["start"])
                timestamp = f"{start // 3600:02}:{(start % 3600) // 60:02}:{start % 60:02}"
                result += f'{item["text"]} "time:{timestamp}" '
            return result
        except Exception as e:
            return f"Error: {e}"
