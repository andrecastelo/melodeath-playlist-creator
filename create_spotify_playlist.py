import metallum
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

from SpotifyAlbum import SpotifyAlbum
from get_released_albums import *

def setup_spotify(**kwargs):
    CLIENT_ID = kwargs.get('client_id', os.getenv('SPOTIFY_CLIENT_ID'))
    CLIENT_SECRET = kwargs.get('client_secret', os.getenv('SPOTIFY_CLIENT_SECRET'))
    REDIRECT_URI = kwargs.get('redirect_uri', os.getenv('SPOTIFY_REDIRECT_URI'))
    scopes = 'user-read-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative'

    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=scopes,
        )
    )


def get_spotify_album_id(album, spotify_api):
    query = "album:{name} artist:{artist}".format(**album)
    response = spotify_api.search(query, offset=0, type='album')

    try:
        for _album in response.get('albums').get('items'):
            album = SpotifyAlbum(_album)
            print("Adding [{}] by [{}]".format(album.name, album.main_artist))
            return album.id
    except:
        return None

def get_spotify_albums(album_ids, spotify_api):
    response = spotify_api.albums(album_ids)

    return [
        SpotifyAlbum(album) for album in response.get('albums')
    ]

def get_track_ids(albums):
    tracks = []
    for album in albums:
        tracks = tracks + album.track_uris

    return tracks

MONTHS = [None, 'January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if __name__ == '__main__':
    load_dotenv()
    print('Welcome! We are going to setup spotify now, you will be redirected to log into your account')
    print('Once that is done, copy the url you were redirected to and paste here')
    spotify_api = setup_spotify()
    current_user = spotify_api.me()
    month = input('Enter the month you want to query (1..12): ')
    year = input('Enter the year your want to query: ')
    print("\nSearching albums on Metal Archives...")
    albums = get_released_albums(month=month, year=year)
    print('\nSearching albums on Spotify...')
    spotify_album_ids = [a for a in [get_spotify_album_id(album, spotify_api) for album in albums] if a is not None]
    print('\nFetching more information about albums...')
    spotify_albums = get_spotify_albums(spotify_album_ids, spotify_api)
    print('\nOrganizing tracklist...')

    playlist_name = input('Enter the playlist name: ')

    spotify_playlist = spotify_api.user_playlist_create(
        current_user.get('id'),
        playlist_name,
        public=True,
        collaborative=False,
        description="Melodic Death Metal, Jan 2021"
    )

    spotify_tracks = get_track_ids(spotify_albums)

    # maximum number of tracks that can be added per request
    max_tracks = 100
    for tracks in [spotify_tracks[i:i + max_tracks] for i in range(0, len(spotify_tracks), max_tracks)]:
        spotify_api.playlist_add_items(spotify_playlist.get('id'), tracks)

    print("\nDone! Check your spotify account")
