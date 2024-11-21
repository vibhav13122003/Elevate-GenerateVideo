from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from dotenv import load_dotenv
from src.video_info import GetVideo
from src.model import Model
from src.prompt import Prompt

load_dotenv()

app = Flask(__name__)

# Allow all origins
CORS(app)

@app.route('/api/video-info', methods=['POST'])
def get_video_info():
    data = request.json
    youtube_url = data.get('youtube_url')

    if not youtube_url:
        return jsonify({"error": "YouTube URL is required"}), 400

    video_id = GetVideo.Id(youtube_url)
    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    video_title = GetVideo.title(youtube_url)
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"

    return jsonify({
        "video_id": video_id,
        "video_title": video_title,
        "thumbnail_url": thumbnail_url
    })


@app.route('/api/summary', methods=['POST'])
def generate_summary():
    data = request.json
    youtube_url = data.get('youtube_url')
    model_name = data.get('model_name')

    if not youtube_url or not model_name:
        return jsonify({"error": "YouTube URL and model name are required"}), 400

    transcript = GetVideo.transcript(youtube_url)
    if model_name == "Gemini":
        summary = Model.google_gemini(transcript=transcript, prompt=Prompt.prompt1())
    elif model_name == "ChatGPT":
        summary = Model.openai_chatgpt(transcript=transcript, prompt=Prompt.prompt1())
    else:
        return jsonify({"error": "Invalid model name"}), 400

    return jsonify({"summary": summary})


@app.route('/api/timestamps', methods=['POST'])
def generate_timestamps():
    data = request.json
    youtube_url = data.get('youtube_url')
    model_name = data.get('model_name')

    if not youtube_url or not model_name:
        return jsonify({"error": "YouTube URL and model name are required"}), 400

    transcript_time = GetVideo.transcript_time(youtube_url)
    youtube_url_full = f"https://youtube.com/watch?v={GetVideo.Id(youtube_url)}"

    if model_name == "Gemini":
        timestamps = Model.google_gemini(transcript_time, Prompt.prompt1(ID='timestamp'), extra=youtube_url_full)
    elif model_name == "ChatGPT":
        timestamps = Model.openai_chatgpt(transcript_time, Prompt.prompt1(ID='timestamp'), extra=youtube_url_full)
    else:
        return jsonify({"error": "Invalid model name"}), 400

    return jsonify({"timestamps": timestamps})


@app.route('/api/transcript', methods=['POST'])
def generate_transcript():
    data = request.json
    youtube_url = data.get('youtube_url')

    if not youtube_url:
        return jsonify({"error": "YouTube URL is required"}), 400

    transcript = GetVideo.transcript(youtube_url)
    return jsonify({"transcript": transcript})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
