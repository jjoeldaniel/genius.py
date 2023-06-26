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

        if album_info["full_title"]:
            self.full_title = album_info["full_title"]
        if album_info["artist"]:
            self.artist = Artist(album_info["artist"])
