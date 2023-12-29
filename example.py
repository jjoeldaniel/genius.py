from geniusdotpy.genius import Genius 
from geniusdotpy.track import Track


def main():
    # Get your client access token from https://genius.com/api-clients
    client_access_token = "token"

    # Create a GeniusBuilder object
    genius = Genius(client_access_token=client_access_token)

    # Search for a track by ID
    track1 = genius.search_track_by_id(378195)
    print(repr(track1))

    # Search artist by ID
    artist1 = genius.search_artist(track1.artist.id)
    print(repr(artist1))

    # Search for a track by query
    track3 = genius.search("Beat It")[0]
    print(repr(track3))

    # Search tracks by artist
    tracks: list[Track] = genius.search_track_by_artist(artist_id=16775)
    track4 = tracks[0]
    print(repr(track4))

    # Retrieve lyrics
    track4.get_lyrics()
    print(track4.lyrics)


if __name__ == "__main__":
    main()
