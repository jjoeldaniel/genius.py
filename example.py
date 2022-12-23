import os
from genius import *
from dotenv import load_dotenv  

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
client_access_token = os.getenv('CLIENT_ACCESS_TOKEN')

genius = Genius(client_id=client_id, client_secret=client_secret, client_access_token=client_access_token)

for track in genius.search('Kendrick Lamar'):
    print(track.release_date())