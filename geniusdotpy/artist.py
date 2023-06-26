import json


class Artist:
    """Genius.com Artist class.

    Only contains always-available information. All other
    information is available in the artist_info JSON object.
    """

    def __init__(self, artist_info: json):
        """Artist constructor.

        Keyword arguments:
            artist_info -- The artist information from Genius.com

        Returns:
            Artist object
        """

        self.artist_info = artist_info
        """JSON object containing artist information."""

        self.api_path = artist_info["api_path"]
        """API path of the artist."""

        self.id = artist_info["id"]
        """Genius.com Artist ID."""

        self.name = artist_info["name"]
        """Artist name."""

        self.url = artist_info["url"]
        """Genius.com URL of the artist."""

    def __str__(self):
        return self.name
