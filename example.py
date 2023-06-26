from geniusdotpy.genius_builder import GeniusBuilder


def main():
    # Get your client access token from https://genius.com/api-clients
    client_access_token = (
        "omEj1v8w4Nx97iaz8KJmGQoiHDvYQah9jHELivHyPYSI1YlRS09-xCcZUz04qOAc"
    )

    # Create a GeniusBuilder object
    genius = GeniusBuilder(client_access_token=client_access_token)

    # Search for a track by ID
    print(genius.search_track_by_id(378195))

    # Search artist by ID
    print(genius.search_artist(16775))

    # Search for a track by query
    print(genius.search("Beat It")[0])

    # Search tracks by artist
    tracks = genius.search_track_by_artist(artist_id=16775)
    print(tracks[0])


if __name__ == "__main__":
    main()
