from track import Track


class Artist:

    def __init__(self, tracks_info):
        self.tracks_info = tracks_info

    def list_tracks(self):
        """Returns a list of Track objects for an Artist"""

        tracks = []

        for track in self.tracks_info:
            track = Track(track_info=track)
            tracks.append(track)

        return tracks
