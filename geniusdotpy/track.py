import datetime
from geniusdotpy.lyrics import Lyrics
from geniusdotpy.album import Album
from geniusdotpy.utils import *


class Track:

    def __init__(self, track_info):
        self.track_info = track_info
        self.artist = track_info['primary_artist']['name']
        self.artist_id = track_info['primary_artist']['id']
        self.title = track_info['title']
        self.path = track_info['path']
        self.title_with_featured = track_info['title_with_featured']
        self.full_title = track_info['full_title']
        self.url = track_info['url']
        self.id = track_info['id']
        self.featured_artists = track_info['featured_artists']
        self.__date = datetime.datetime(1, 1, 1)
        self.lyrics = Lyrics(track_url=self.url).content
        self.lyrics_by_line = self.lyrics.split('\n')

        if 'album' in track_info:
            self.album = Album(album_info=track_info['album'])

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

        if 'media' in track_info:
            for media in track_info['media']:
                if media['provider'] == 'youtube':
                    self.youtube_url = media['url']
                if media['provider'] == 'spotify':
                    self.spotify_url = media['url']
                if media['provider'] == 'soundcloud':
                    self.soundcloud_url = media['url']

    def __str__(self):
        return self.full_title

    def to_json(self):
        """Returns a JSON object of the track"""

        return format_json(self.track_info)

    def release_date(self):
        """Returns the release date of the track as a datetime object"""

        if self.__date.year != 1:
            return self.__date

        year = self.track_info['release_date_components']['year']
        month = self.track_info['release_date_components']['month']
        day = self.track_info['release_date_components']['day']
        self.__date = datetime.datetime(year, month, day)

        return self.__date
