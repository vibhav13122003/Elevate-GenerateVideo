def format_seconds_to_timestamp(seconds):
    """Converts seconds into HH:MM:SS format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def generate_youtube_timestamp_link(video_id, timestamp):
    """
    Generates a clickable YouTube link with a timestamp.

    Args:
        video_id (str): The YouTube video ID.
        timestamp (str): The timestamp in HH:MM:SS format.

    Returns:
        str: A YouTube link with the embedded timestamp.
    """
    try:
        h, m, s = map(int, timestamp.split(":"))
        total_seconds = h * 3600 + m * 60 + s
        return f"https://youtube.com/watch?v={video_id}&t={total_seconds}s"
    except ValueError:
        return "Error: Invalid timestamp format. Use HH:MM:SS."
