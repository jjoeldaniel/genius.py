from geniusdotpy.utils import *

class Album:

    def __init__(self, album_info):
        self.album_info = album_info
        self.id = album_info['id']
        self.url = album_info['url']
        self.path = album_info['api_path']

        if 'cover_art_url' in album_info:
            self.cover_art_url = album_info['cover_art_url']

        # Fallback name to full_title if name is not present and vice versa
        if 'name' in album_info:
            self.name = album_info['name']
        else:
            self.name = album_info['full_title']

        if 'full_title' in album_info:
            self.full_title = album_info['full_title']
        else:
            self.full_title = album_info['name']


    def __str__(self):
        return self.name

    def to_json(self):
        """Convert album info to JSON.
        
        Returns:
            JSON object
        """

        return format_json(self.album_info)
