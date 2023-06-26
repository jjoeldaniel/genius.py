from geniusdotpy.genius_builder import GeniusBuilder
from geniusdotpy.track import Track


def main():
    # Get your client access token from https://genius.com/api-clients
    client_access_token = "token"

    # Create a GeniusBuilder object
    genius = GeniusBuilder(client_access_token=client_access_token)

    # Search for a track by ID
    print(genius.search_track_by_id(378195))

    # Search artist by ID
    print(genius.search_artist(16775))

    # Search for a track by query
    print(genius.search("Beat It")[0])

    # Search tracks by artist
    tracks: list[Track] = genius.search_track_by_artist(artist_id=16775)
    print(tracks[0])
    print(tracks[0].lyrics)


if __name__ == "__main__":
    main()
