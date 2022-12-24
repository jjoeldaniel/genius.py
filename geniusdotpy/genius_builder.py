import requests
from geniusdotpy.track import Track
from geniusdotpy.artist import Artist


class GeniusBuilder:
    endpoint = 'https://api.genius.com'

    def __init__(self, client_id, client_secret, client_access_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_access_token = client_access_token

    def search_by_id(self, track_id):
        """Returns a Track object with the given track ID"""

        endpoint = f'{self.endpoint}/songs/{track_id}'
        headers = {'Authorization': f'Bearer {self.client_access_token}'}

        response = requests.get(endpoint, headers=headers)
        return Track(track_info=response.json()['response']['song'])

    def search(self, query):
        """Returns a list of Track objects with the given query"""

        endpoint = f'{self.endpoint}/search'
        data = {'q': query}
        headers = {'Authorization': f'Bearer {self.client_access_token}'}

        response = requests.get(endpoint, params=data, headers=headers)

        tracks = []

        for hits in response.json()['response']['hits']:
            track = Track(track_info=hits['result'])
            tracks.append(track)

        return tracks

    def search_artist(self, artist_id):
        """Returns an Artist object with the given artist ID"""

        endpoint = f'{self.endpoint}/artists/{artist_id}/songs'
        headers = {'Authorization': f'Bearer {self.client_access_token}'}

        response = requests.get(endpoint, headers=headers)
        tracks_info = response.json()['response']['songs']

        endpoint = f'{self.endpoint}/artists/{artist_id}'
        response = requests.get(endpoint, headers=headers)
        artist_info = response.json()['response']['artist']

        return Artist(artist_info=artist_info, tracks_info=tracks_info)
