import datetime
import json
from geniusdotpy.album import Album
from geniusdotpy.artist import Artist


class Track:
    def __init__(self, track_info: json):
        """Track constructor.

        Keyword arguments:
            track_info -- JSON object containing track info
        """

        self._track_info = track_info
        self.api_path = track_info["api_path"]
        self.id = track_info["id"]
        self.url = track_info["url"]
        self.title = track_info["title"]
        self.artist = Artist(track_info["primary_artist"])

        # Possibly null values
        self.release_date = None
        self.youtube_url = None
        self.spotify_url = None
        self.soundcloud_url = None
        self.album = None

        if "album" in track_info:
            self.album = Album(track_info["album"])

        if "release_date" in track_info:
            self.release_date = datetime.datetime.strptime(
                track_info["release_date"], "%Y-%m-%d"
            )

        if "media" in track_info:
            for provider in track_info["media"]:
                if provider["provider"] == "youtube":
                    self.youtube_url = provider["url"]
                elif provider["provider"] == "spotify":
                    self.spotify_url = provider["url"]
                elif provider["provider"] == "soundcloud":
                    self.soundcloud_url = provider["url"]

    def __str__(self):
        return f"{self.title} by {self.artist.name}"
