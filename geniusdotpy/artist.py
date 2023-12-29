import json

class Artist:
    """Genius.com Artist class.

    Only contains always-available information. All other
    information is available in the artist_info JSON object.
    """

    def __init__(self, artist_info: dict):
        """Artist constructor.

        Keyword arguments:
            artist_info -- The artist information from Genius.com

        Returns:
            Artist object
        """

        self.api_path: str = artist_info["api_path"]
        """API path of the artist."""

        self.id: str = artist_info["id"]
        """Genius.com Artist ID."""

        self.name: str = artist_info["name"]
        """Artist name."""

        self.url: str = artist_info["url"]
        """Genius.com URL of the artist."""

        self.artist_info: dict[str, str] = {
            "api_path": self.api_path,
            "id": self.id,
            "name": self.name,
            "url": self.url,
        }
        """Dictionary containing artist information."""

        self.json = json.dumps(self.artist_info, indent=2)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.json