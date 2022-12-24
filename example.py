from geniusdotpy.genius_builder import GeniusBuilder

# Get your client ID, client secret, and client access token from https://genius.com/api-clients
client_id="Yt3PHylqmH84fnroVLfj85G0jO_u3ytyRfrBwd5OK7G40pro2kfzbLoBn0FpG33v"
client_secret="4lIFWRO-6Va200lMq-1jcu3jBZS5sXZ6PtJ1r7LzGfAtoTKN_--bVLiQlrFk6BnzWU3zgkzIrkOGuDF_H0ETOA"
client_access_token="I8riIsMnEjEz49W6J1S6J0ni6wTPM4lvny4MOFavO3UumBHlikIIdkpm6y-Cmz14"

# Create a GeniusBuilder object
genius = GeniusBuilder(client_id=client_id, client_secret=client_secret, client_access_token=client_access_token)

# Returns a list of songs containing query
print(genius.search(query='Kendrick Lamar')[0])

# Returns an Artist object containing all songs by artist
artist = genius.search_artist(artist_id=16775)
print(artist.tracks[0])

# Returns song matching song ID
track = genius.search_by_id(378195)
print(track)

# Prints the lyrics of the song
print(track.lyrics)