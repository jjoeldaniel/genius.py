from bs4 import BeautifulSoup
import requests


class Lyrics:

    def __init__(self, track_url):
        html = requests.get(track_url).content
        soup = BeautifulSoup(html, 'html.parser')
        self.content = soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-6 YYrds').get_text(separator='\n')
        self.content_by_line = self.content.split('\n')
