import re

def clean_text(text):
    """Cleans input text by removing unnecessary whitespace and special characters."""
    return re.sub(r'\s+', ' ', text).strip()

def validate_url(url):
    """Validates if the given string is a proper YouTube URL."""
    youtube_patterns = [
        r'^https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+',
        r'^https?://youtu\.be/[\w-]+'
    ]
    return any(re.match(pattern, url) for pattern in youtube_patterns)
