import datetime
from geniusdotpy import utils
from geniusdotpy.album import Album
from geniusdotpy.artist import Artist
import json


class Track:
    def __init__(self, track_info: dict):
        """Track constructor.

        Keyword arguments:
            track_info -- JSON object containing track info
        """

        """JSON object containing track information."""

        self.api_path: str = track_info["api_path"]
        """API path of the track."""

        self.id: str = track_info["id"]
        """Genius.com Track ID.""" ""

        self.url: str = track_info["url"]
        """Genius.com URL of the track."""

        self.lyrics: None | str = None
        """Track lyrics."""

        self.title: str = track_info["title"]
        """Track title."""

        self.artist: Artist = Artist(track_info["primary_artist"])
        """Track artist."""

        self.release_date: None | datetime.datetime = None
        """Track release date."""

        self.youtube_url: None | str = None
        """Track YouTube URL."""

        self.spotify_url: None | str = None
        """Track Spotify URL."""

        self.soundcloud_url: None | str = None
        """Track Soundcloud URL."""

        self.album: None | Album = None
        """Track album."""

        if "album" in track_info:
            self.album = Album(track_info["album"])

        if "release_date" in track_info:
            self.release_date = datetime.datetime.strptime(
                track_info["release_date"], "%Y-%m-%d"
            )

        if "media" in track_info:
            for provider in track_info["media"]:
                match provider["provider"]:
                    case "youtube":
                        self.youtube_url = provider["url"]
                    case "spotify":
                        self.spotify_url = provider["url"]
                    case "soundcloud":
                        self.soundcloud_url = provider["url"]
        

        self.track_info: dict = {
            "api_path": self.api_path,
            "id": self.id,
            "url": self.url,
            "lyrics": self.lyrics,
            "title": self.title,
            "artist": self.artist.artist_info,
            "release_date": str(self.release_date),
            "youtube_url": self.youtube_url,
            "spotify_url": self.spotify_url,
            "soundcloud_url": self.soundcloud_url,
        }

        if self.album:
            self.track_info["album"] = self.album.album_info
        else:
            self.track_info["album"] = None

        self.json = json.dumps(self.track_info, indent=2)

    def get_lyrics(self) -> None | str:
        """Retrieves the lyrics of the track."""

        if not self.lyrics:
            self.lyrics = utils.retrieve_lyrics(self.url)
        
        return self.lyrics

    def __str__(self):
        return f"{self.title} by {self.artist.name}"

    def __repr__(self):
        return self.json