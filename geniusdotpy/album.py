from geniusdotpy.utils import *

class Album:

    def __init__(self, album_info):
        self.album_info = album_info
        self.id = album_info['id']
        self.name = album_info['name']
        self.url = album_info['url']
        self.path = album_info['api_path']
        self.cover_art_url = album_info['cover_art_url']

    def __str__(self):
        return self.name

    def to_json(self):
        """Returns a JSON object of the album"""

        return format_json(self.album_info)
