import datetime

class Track:

    def __init__(self, track_info):
        self.track_info = track_info
        self.name = track_info['title_with_featured']
        self.artist = track_info['primary_artist']['name']
        self.title = track_info['title']
        self.title_with_featured = track_info['title_with_featured']
        self.full_title = track_info['full_title']
        self.url = track_info['url']
        self.id = track_info['id']
        self.language = track_info['language']
        self.featured_artists = track_info['featured_artists']
        self.header_image_thumbnail_url = track_info['header_image_thumbnail_url']
        self.header_image_url = track_info['header_image_url']
        self.path = track_info['path']
        self.song_art_image_thumbnail_url = track_info['song_art_image_thumbnail_url']
        self.art_image_url = track_info['song_art_image_url']
        self.page_views = track_info['stats']['pageviews']

    def __str__(self):
        return self.full_title

    def get_artist_id(self):
        return self.track_info['primary_artist']['id']

    def release_date(self):
        year = self.track_info['release_date_components']['year']
        month = self.track_info['release_date_components']['month']
        day = self.track_info['release_date_components']['day']

        date = datetime.datetime(year, month, day)

        return date