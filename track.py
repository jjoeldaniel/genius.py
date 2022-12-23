import datetime

class Track:

    def __init__(self, track_info):
        self.track_info = track_info
        self.name = track_info['result']['title_with_featured']
        self.artist = track_info['result']['primary_artist']['name']
        self.full_title = track_info['result']['full_title']
        self.url = track_info['result']['url']

    def __str__(self):
        return self.full_title

    def name(self):
        return self.name

    def artist(self):
        return self.artist

    def full_title(self):
        return self.full_title

    def url(self):
        return self.url

    def release_date(self):
        year = self.track_info['result']['release_date_components']['year']
        month = self.track_info['result']['release_date_components']['month']
        day = self.track_info['result']['release_date_components']['day']

        date = datetime.datetime(year, month, day)

        return date