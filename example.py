from geniusdotpy.genius_builder import GeniusBuilder

# Get your client ID, client secret, and client access token from https://genius.com/api-clients
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
client_access_token = 'CLIENT_ACCESS_TOKEN'

# Create a GeniusBuilder object
genius = GeniusBuilder(client_id=client_id, client_secret=client_secret, client_access_token=client_access_token)

# Returns a list of songs containing query
print(genius.search(query='Kendrick Lamar')[0])

# Returns song matching song ID
print(genius.search_by_id(378195))

# Returns an Artist object containing all songs by artist
artist = genius.search_artist(artist_id=16775)
for song in artist.tracks:
    print(song)