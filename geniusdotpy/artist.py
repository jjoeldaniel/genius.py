from geniusdotpy.track import Track


class Artist:

    def __init__(self, tracks_info):
        self.tracks_info = tracks_info
        self.tracks = [Track(track_info=track_info) for track_info in self.tracks_info]
