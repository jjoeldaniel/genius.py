import datetime

class Track:

    def __init__(self, track_info):
        self.track_info = track_info
        self.name = track_info['title_with_featured']
        self.artist = track_info['primary_artist']['name']
        self.title = track_info['title']
        self.path = track_info['path']
        self.title_with_featured = track_info['title_with_featured']
        self.full_title = track_info['full_title']
        self.url = track_info['url']
        self.id = track_info['id']
        self.featured_artists = track_info['featured_artists']

        if 'language' in track_info:
            self.language = track_info['language']
        else:
            self.language = None
        
        if 'header_image_thumbnail_url' in track_info:
            self.header_image_thumbnail_url = track_info['header_image_thumbnail_url']
        else:
            self.header_image_thumbnail_url = None

        if 'header_image_url' in track_info:
            self.header_image_url = track_info['header_image_url']
        else:
            self.header_image_url = None

        if 'song_art_image_thumbnail_url' in track_info:
            self.song_art_image_thumbnail_url = track_info['song_art_image_thumbnail_url']
        else:
            self.song_art_image_thumbnail_url = None
        
        if 'song_art_image_url' in track_info:
            self.art_image_url = track_info['song_art_image_url']
        else:
            self.art_image_url = None

        if 'pageviews' in track_info['stats']:
            self.page_views = track_info['stats']['pageviews']
        else:
            self.page_views = None

    def __str__(self):
        return self.full_title

    def get_artist_id(self):
        """Returns the artist ID of the primary artist of the track"""
        return self.track_info['primary_artist']['id']

    def release_date(self):
        """Returns the release date of the track as a datetime object"""

        if 'release_date' not in self.track_info:
            return datetime.datetime(1, 1, 1)

        year = self.track_info['release_date_components']['year']
        month = self.track_info['release_date_components']['month']
        day = self.track_info['release_date_components']['day']

        date = datetime.datetime(year, month, day)

        return date