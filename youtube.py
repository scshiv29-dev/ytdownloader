from pytube import YouTube


class download:
    def __init__(self, url):
        self.url = url

    def details(self):
        self.yt = YouTube(url)
        self.title = self.yt.title
        self.thumbnail = self.yt.thumbnail_url
        self.streams = self.yt.streams

    def download(self, itag, url):
        yt = YouTube(url)
        steam = yt.streams.get_by_itag(itag)
        steam.download()
        return {"message": "Downloading"}
