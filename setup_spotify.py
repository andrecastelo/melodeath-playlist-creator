import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

DEFAULT_SCOPES = "user-read-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative"


def setup_spotify(**kwargs):
    CLIENT_ID = kwargs.get("client_id", os.getenv("SPOTIFY_CLIENT_ID"))
    CLIENT_SECRET = kwargs.get("client_secret", os.getenv("SPOTIFY_CLIENT_SECRET"))
    REDIRECT_URI = kwargs.get("redirect_uri", os.getenv("SPOTIFY_REDIRECT_URI"))
    scopes = kwargs.get("scopes", DEFAULT_SCOPES)

    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=scopes,
        )
    )
