from track import *


class Artist:

    def __init__(self, tracks_info):
        self.tracks_info = tracks_info
        self.tracks = []

        for track in self.tracks_info:
            track = Track(track_info=track)
            self.tracks.append(track)
