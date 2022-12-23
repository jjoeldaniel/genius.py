import requests
import json
from track import Track

class Genius:

    endpoint = 'https://api.genius.com'

    def __init__(self, client_id, client_secret, client_access_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_access_token = client_access_token

    def search(self, query):
        endpoint = f'{self.endpoint}/search'
        data = {'q': query}
        headers = {'Authorization': f'Bearer {self.client_access_token}'}

        response = requests.get(endpoint, params=data, headers=headers)

        tracks = []

        for hits in response.json()['response']['hits']:
            track = Track(track_info=hits)
            tracks.append(track)

        return tracks