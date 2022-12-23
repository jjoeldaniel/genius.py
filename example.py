import os
from genius_builder import *
from dotenv import load_dotenv

# Example uses dotenv to load environment variables from .env file
# See https://github.com/cdimascio/dotenv-java
load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
client_access_token = os.getenv('CLIENT_ACCESS_TOKEN')

genius = GeniusBuilder(client_id=client_id, client_secret=client_secret, client_access_token=client_access_token)

for track in genius.search(query='Kendrick Lamar'):
    print(track)

print(genius.search_by_id(378195).page_views)