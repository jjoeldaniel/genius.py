import requests
from geniusdotpy.track import Track
from geniusdotpy.artist import Artist
from geniusdotpy.album import Album


class GeniusBuilder:
    endpoint = "https://api.genius.com"

    def __init__(self, client_access_token):
        """GeniusBuilder constructor.

        Keyword arguments:
            client_access_token -- The client access token from https://genius.com/api-clients

        Returns:
            GeniusBuilder object
        """

        self.client_access_token = client_access_token

    def search_by_id(self, track_id):
        """Search for a track by ID.

        Keyword arguments:
            track_id -- The ID of the song

        Returns:
            Track object
        """

        endpoint = f"{self.endpoint}/songs/{track_id}"
        headers = {"Authorization": f"Bearer {self.client_access_token}"}

        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        return Track(track_info=response.json()["response"]["song"])

    def search(self, query):
        """Search for a track by query.

        Keyword arguments:
            query -- The query to search for

        Returns:
            List of Track objects
        """

        endpoint = f"{self.endpoint}/search"
        data = {"q": query}
        headers = {"Authorization": f"Bearer {self.client_access_token}"}

        response = requests.get(endpoint, params=data, headers=headers)
        response.raise_for_status()

        tracks = []

        for hits in response.json()["response"]["hits"]:
            track = Track(track_info=hits["result"])
            tracks.append(track)

        return tracks

    def search_artist(self, artist_id):
        """Search for an artist by ID.

        Keyword arguments:
            artist_id -- The ID of the artist

        Returns:
            Artist object
        """

        endpoint = f"{self.endpoint}/artists/{artist_id}/songs"
        headers = {"Authorization": f"Bearer {self.client_access_token}"}

        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        tracks_info = response.json()["response"]["songs"]

        endpoint = f"{self.endpoint}/artists/{artist_id}"
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        artist_info = response.json()["response"]["artist"]

        return Artist(artist_info=artist_info, tracks_info=tracks_info)

    def search_album(self, album_id):
        """Search for an album by ID.

        Keyword arguments:
            album_id -- The ID of the album

        Returns:
            Album object
        """

        endpoint = f"{self.endpoint}/albums/{album_id}"
        headers = {"Authorization": f"Bearer {self.client_access_token}"}

        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        album_info = response.json()["response"]["album"]

        return Album(album_info=album_info)
