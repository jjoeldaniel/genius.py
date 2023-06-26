import requests
from geniusdotpy.artist import Artist
from geniusdotpy.track import Track
from geniusdotpy.utils import SortType


class GeniusBuilder:
    endpoint = "https://api.genius.com"
    """Genius API endpoint"""

    def __init__(self, client_access_token: str):
        """GeniusBuilder constructor.

        Keyword arguments:
            client_access_token -- The client access token from https://genius.com/api-clients

        Returns:
            GeniusBuilder object
        """

        self.headers = {"Authorization": f"Bearer {client_access_token}"}

    def search_track_by_id(self, track_id: str):
        """Search for a track by ID.

        Keyword arguments:
            track_id -- The ID of the track

        Returns:
            Track object
        """

        endpoint = f"{self.endpoint}/songs/{track_id}"

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()

        return Track(track_info=response.json()["response"]["song"])

    def search_artist(self, artist_id: str):
        """Search for an artist by ID.

        Keyword arguments:
            artist_id -- The ID of the artist

        Returns:
            Artist object
        """

        endpoint = f"{self.endpoint}/artists/{artist_id}"

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()

        return Artist(artist_info=response.json()["response"]["artist"])

    def search(self, query: str) -> list[Track]:
        """Search for a track by query.

        Keyword arguments:
            query -- The query to search for

        Returns:
            Track object
        """

        endpoint = f"{self.endpoint}/search?q={query}"

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()

        tracks: list[Track] = list()

        for hits in response.json()["response"]["hits"]:
            tracks.append(Track(track_info=hits["result"]))

        return tracks

    def search_track_by_artist(
        self, artist_id: int, sort=SortType.TITLE, page=1, per_page=20
    ) -> list:
        endpoint = f"{self.endpoint}/artists/{artist_id}/songs?sort={sort.value}&per_page={per_page}&page={page}"
        tracks = list()

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()

        for song in response.json()["response"]["songs"]:
            tracks.append(Track(track_info=song))

        return tracks
