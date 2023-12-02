from dotenv import load_dotenv
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

DEFAULT_SCOPES = "user-read-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative"


def setup_spotify(**kwargs):
    load_dotenv()
    CLIENT_ID = kwargs.get("client_id", os.getenv("SPOTIFY_CLIENT_ID"))
    CLIENT_SECRET = kwargs.get("client_secret", os.getenv("SPOTIFY_CLIENT_SECRET"))
    REDIRECT_URI = kwargs.get("redirect_uri", "http://localhost")
    scopes = kwargs.get("scopes", DEFAULT_SCOPES)

    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=scopes,
        )
    )


class SpotifyApi:
    api = None

    def __init__(self):
        load_dotenv()
        self.api = self.setup()

    def setup(self, **kwargs):
        CLIENT_ID = kwargs.get("client_id", os.getenv("SPOTIFY_CLIENT_ID"))
        CLIENT_SECRET = kwargs.get("client_secret", os.getenv("SPOTIFY_CLIENT_SECRET"))
        REDIRECT_URI = kwargs.get("redirect_uri", "http://localhost")
        scopes = kwargs.get("scopes", DEFAULT_SCOPES)

        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                scope=scopes,
            )
        )
