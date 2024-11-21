from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.video_info import GetVideo
from src.model import Model
from src.prompt import Prompt
from constant import SERVER_URL, PORT, ENV

load_dotenv()

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/video-info")
async def get_video_info(youtube_url: str):
    if not youtube_url:
        raise HTTPException(status_code=400, detail="YouTube URL is required")
    
    video_id = GetVideo.Id(youtube_url)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")
    
    video_title = GetVideo.title(youtube_url)
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"

    return {"video_id": video_id, "video_title": video_title, "thumbnail_url": thumbnail_url}


@app.post("/api/summary")
async def generate_summary(youtube_url: str, model_name: str):
    if not youtube_url or not model_name:
        raise HTTPException(status_code=400, detail="YouTube URL and model name are required")

    transcript = GetVideo.transcript(youtube_url)
    if model_name == "Gemini":
        summary = Model.google_gemini(transcript=transcript, prompt=Prompt.prompt1())

    else:
        raise HTTPException(status_code=400, detail="Invalid model name")

    return {"summary": summary}


@app.post("/api/timestamps")
async def generate_timestamps(youtube_url: str, model_name: str):
    if not youtube_url or not model_name:
        raise HTTPException(status_code=400, detail="YouTube URL and model name are required")

    transcript_time = GetVideo.transcript_time(youtube_url)
    youtube_url_full = f"https://youtube.com/watch?v={GetVideo.Id(youtube_url)}"

    if model_name == "Gemini":
        timestamps = Model.google_gemini(transcript_time, Prompt.prompt1(ID="timestamp"), extra=youtube_url_full)

    else:
        raise HTTPException(status_code=400, detail="Invalid model name")

    return {"timestamps": timestamps}


@app.post("/api/transcript")
async def generate_transcript(youtube_url: str):
    if not youtube_url:
        raise HTTPException(status_code=400, detail="YouTube URL is required")
    
    transcript = GetVideo.transcript(youtube_url)
    return {"transcript": transcript}


# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))
