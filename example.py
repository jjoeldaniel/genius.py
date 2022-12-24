from geniusdotpy.genius_builder import GeniusBuilder

# Get your client ID, client secret, and client access token from https://genius.com/api-clients
client_id="id"
client_secret="secret"
client_access_token="token"

# Create a GeniusBuilder object
genius = GeniusBuilder(client_id=client_id, client_secret=client_secret, client_access_token=client_access_token)

# Returns a list of songs containing query
print(genius.search(query='Kendrick Lamar')[0])

# Returns an Artist object containing all songs by artist
artist = genius.search_artist(artist_id=16775)
print(artist.tracks[0])

# Returns song matching song ID
track = genius.search_by_id(378195)
print(f'{track}\nAlbum: {track.album}')

# Prints the lyrics of the song
print(f'Lyrics:\n{track.lyrics}')