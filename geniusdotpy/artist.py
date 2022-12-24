from geniusdotpy.track import Track


class Artist:

    def __init__(self, artist_info, tracks_info):
        self.artist_info = artist_info
        self.tracks_info = tracks_info
        self.tracks = [Track(track_info=track_info) for track_info in self.tracks_info]
