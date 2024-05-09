from fastapi import FastAPI


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000" "http://localhost:8080",
       "http://c0kc4ko.95.217.220.139.sslip.io",
    "https://c0kc4ko.95.217.220.139.sslip.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pytube import YouTube


@app.get("/")
async def root():
    return {"message": "Welcome to Youtube Downloader API"}


@app.get("/get/{url}")
async def details(url):
    strw = "https://www.youtube.com/watch?v=" + url
    print(strw)
    yt =YouTube(strw)
    print(yt)
    title = yt.title
    stream = yt.streams
    thumbnail = yt.thumbnail_url
    return {
        "title": title,
        "thumbnail": thumbnail,
        "stream": stream.fmt_streams,
    }
