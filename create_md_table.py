import metallum
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

from SpotifyAlbum import SpotifyAlbum
from get_released_albums import *

def setup_spotify(**kwargs):
    CLIENT_ID = kwargs.get('client_id', os.getenv('SPOTIFY_CLIENT_ID'))
    CLIENT_SECRET = kwargs.get('client_secret', os.getenv('SPOTIFY_CLIENT_SECRET'))

    return spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        )
    )


def search_album(album, spotify_api):
    query = "album:{name} artist:{artist}".format(**album)
    response = spotify_api.search(query, offset=0, type='album')

    try:
        for album in response.get('albums').get('items'):
            return SpotifyAlbum(album)
    except:
        return None


if __name__ == '__main__':
    year = input('Year [2001]: ')
    year = year if year else 2021
    month = input('Month [1]: ')
    month = month if month else 1
    albums = get_released_albums(year=year, month=month)
    load_dotenv()
    spotify_api = setup_spotify()

    print("Band | Album | Genre | Date | Playlist")
    print(":----|:------|:------|-----:|:--------")
    for a in albums:
        spotify_album = search_album(a, spotify_api)

        if (spotify_album):
            print("{artist} | {name} | {genre} | {date} | {playlist}".format(
                artist=spotify_album.main_artist,
                name=spotify_album.name,
                genre=a.get('genre', '-'),
                date=spotify_album.release_date,
                playlist=spotify_album.external_url,
            ))
        else:
            print("{artist} | {name} | {genre} | {date} | -".format(**a))