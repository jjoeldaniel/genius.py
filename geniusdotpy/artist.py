from geniusdotpy.track import Track
from geniusdotpy.utils import format_json


class Artist:
    def __init__(self, artist_info, tracks_info):
        self.artist_info = artist_info
        self.tracks_info = tracks_info
        self.tracks = [Track(track_info=track_info) for track_info in self.tracks_info]
        self.id = self.artist_info["id"]
        self.name = self.artist_info["name"]
        self.url = self.artist_info["url"]
        self.path = self.artist_info["api_path"]

    def to_json(self):
        """Convert artist info to JSON.

        Returns:
            JSON object
        """

        return format_json(self.artist_info)
