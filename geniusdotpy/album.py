import json
from geniusdotpy.artist import Artist


class Album:
    """Album class"""

    def __init__(self, album_info: json):
        self.album_info = album_info
        self.name = album_info["name"]
        self.url = album_info["url"]

        # Default `full_title` to name
        self.full_title = album_info["name"]

        # Possibly null values
        self.artist = None

        if "full_title" in album_info:
            self.full_title = album_info["full_title"]
        if "artist" in album_info:
            self.artist = Artist(album_info["artist"])
