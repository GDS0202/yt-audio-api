# main.py
from fastapi import FastAPI, HTTPException
from yt_dlp import YoutubeDL

app = FastAPI()

@app.get("/audio")
def get_audio_url(video_id: str):
    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'format': 'bestaudio[ext=m4a]/bestaudio',
            'cookiefile': 'cookies.txt'
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            return {"url": info['url']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
