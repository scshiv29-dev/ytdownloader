from fastapi import FastAPI

from youtube import download
from deta import Deta

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000" "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000" "http://localhost:8080",
    "http://ytmagic.ml",
    "https://ytmagic.ml",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pytube import YouTube

deta = Deta("c0ovi4pb_oJbusvgiZNrfNuZxJUYePoFNdmLQVKth")
drive = deta.Drive("songs")


@app.get("/")
async def root():
    return {"message": "Welcome to Youtube Downloader API"}


@app.get("/get/{url}")
async def details(url):
    strw = "https://www.youtube.com/watch?v=" + url
    print(strw)
    yt = YouTube(strw)
    print(yt)
    title = yt.title
    stream = yt.streams
    thumbnail = yt.thumbnail_url
    return {
        "title": title,
        "thumbnail": thumbnail,
        "stream": stream.fmt_streams,
    }
