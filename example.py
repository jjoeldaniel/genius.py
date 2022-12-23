import os
from genius_builder import *
from dotenv import load_dotenv

# Example uses dotenv to load environment variables from .env file
# See https://pypi.org/project/python-dotenv/
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
client_access_token = os.getenv('CLIENT_ACCESS_TOKEN')

genius = GeniusBuilder(client_id=client_id, client_secret=client_secret, client_access_token=client_access_token)

print(genius.search(query='Kendrick Lamar')[0])
print(genius.search_by_id(378195))

artist = genius.search_artist(artist_id=16775)
for song in artist.list_tracks():
    print(song)