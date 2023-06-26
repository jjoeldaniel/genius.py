from geniusdotpy.genius_builder import GeniusBuilder


def main():
    
    # Get your client access token from https://genius.com/api-clients
    client_access_token = "token"

    # Create a GeniusBuilder object
    genius = GeniusBuilder(client_access_token=client_access_token)

    track = genius.search_track_by_id(track_id=378195)
    print(track.release_date)


if __name__ == "__main__":
    main()