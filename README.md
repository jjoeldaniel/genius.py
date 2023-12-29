# **genius.py**

[![PyPI version](https://img.shields.io/pypi/v/geniusdotpy)](https://pypi.org/project/geniusdotpy/)
[![Python 3.x version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://www.python.org/downloads/)
[![Documentation](https://img.shields.io/badge/documentation-8A2BE2)](https://jjoeldaniel.github.io/genius.py/)
[![Downloads](https://static.pepy.tech/badge/geniusdotpy)](https://pepy.tech/project/geniusdotpy)

> Python wrapper for Genius API

With genius.py, enjoy an easy-to-use interface to interact with [Genius API](https://docs.genius.com)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Install](#install)
- [Getting Started](#getting-started)
- [References](#references)

---

## Features

- Feature rich interface
- Easy to use
- Lyrics web scraper

## Install

```bash
pip install geniusdotpy
```

## Getting Started

To get started...

1. Get your Client Access Token [here](https://genius.com/api-clients)

2. Create a new *Genius* object

    ```python
    from geniusdotpy.genius import Genius

    # Get your client access token from https://genius.com/api-clients
    client_access_token = "token"

    # Create a GeniusBuilder object
    genius = Genius(client_access_token=client_access_token)

    # Search for a track by ID
    track1 = genius.search_track_by_id(378195)
    print(repr(track1))

    # Search artist by ID
    artist1 = genius.search_artist(track1.artist.id)
    print(repr(artist1))

    # Search for a track by query
    track3 = genius.search("Beat It")[0]
    print(repr(track3))

    # Search tracks by artist
    tracks: list[Track] = genius.search_track_by_artist(artist_id=16775)
    track4 = tracks[0]
    print(repr(track4))

    # Retrieve lyrics
    track4.get_lyrics()
    print(track4.lyrics)
    ```

3. ???

4. Profit

## References

[Genius API](https://docs.genius.com)

---

Created with 💖 by [*jjoeldaniel*](https://github.com/jjoeldaniel)
