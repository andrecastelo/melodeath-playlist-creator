from dotenv import load_dotenv

from Table import Table
from SpotifyAlbum import SpotifyAlbum
from get_released_albums import *
from setup_spotify import setup_spotify


def search_album(album, spotify_api):
    query = "album:{name} artist:{artist}".format(**album)
    response = spotify_api.search(query, offset=0, type="album")

    try:
        album = response.get("albums").get("items").pop(0)
        spotify_album = SpotifyAlbum(album)
        spotify_album.main_artist = spotify_api.artist(spotify_album.main_artist_uri)

        return spotify_album

    except:
        return None


def build_md_table(albums):
    markdown_table = Table(albums)
    markdown_table.print_markdown()


def main_app():
    year = input("Starting year [2021]: ")
    year = year if year else 2021
    month = input("Month [1]: ")
    month = month if month else 1
    print("Fetching released albums for the period on Metal Archives...")
    albums = get_released_albums(year=year, month=month)

    print("Loading environment...")
    load_dotenv()

    print("Setting up Spotify API...")
    spotify_api = setup_spotify()

    for album in albums:
        spotify_album = search_album(album, spotify_api)
        if spotify_album:
            album["spotify_album"] = spotify_album

    build_md_table(albums)


if __name__ == "__main__":
    main_app()
