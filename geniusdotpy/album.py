from geniusdotpy.artist import Artist


class Album:
    """Album class"""

    def __init__(self, album_info: dict):
        self.album_info = album_info
        """JSON object containing album information."""

        self.name: str = album_info["name"]
        """Album name"""

        self.url: str = album_info["url"]
        """Album URL"""

        # Default `full_title` to name
        self.full_title: str = album_info["name"]
        """Album full title"""

        # Possibly null values
        self.artist = None
        """Album artist"""

        if "full_title" in album_info:
            self.full_title = album_info["full_title"]
        if "artist" in album_info:
            self.artist = Artist(album_info["artist"])
