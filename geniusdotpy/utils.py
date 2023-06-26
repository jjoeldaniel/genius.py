import json
from bs4 import BeautifulSoup
import requests


def format_json(json_object):
    """Formats JSON object to be more readable

    Keyword arguments:
        json_object -- The JSON object to format

    Returns:
        JSON object
    """
    return json.dumps(json_object, indent=2)


def retrieve_lyrics(track_url):
        html = requests.get(track_url).content
        soup = BeautifulSoup(html, "html.parser")

        return soup.find(
            "div", class_="Lyrics__Container-sc-1ynbvzw-5"
        ).get_text(separator="\n")