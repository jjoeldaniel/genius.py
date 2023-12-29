from enum import Enum
from bs4 import BeautifulSoup
import requests


class SortType(Enum):
    """Enum for sorting Genius search results"""

    POPULARITY = "popularity"
    TITLE = "title"


def retrieve_lyrics(track_url: str):
    """
    Retrieves the lyrics of a song from Genius.

    Keyword arguments:
        track_url -- The URL of the song
    """

    html = requests.get(track_url).content
    soup = BeautifulSoup(html, "html.parser")
    res = soup.find("div", class_=lambda x: x and x.startswith("Lyrics__Container"))

    if res:
        return res.get_text(separator="\n")
    else:
        return None