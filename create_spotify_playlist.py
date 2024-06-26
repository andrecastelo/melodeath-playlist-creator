from dotenv import load_dotenv

from get_released_albums import *
from setup_spotify import setup_spotify
from SpotifyAlbum import SpotifyAlbum


def get_spotify_album_id(album, spotify_api):
    query = "album:{name} artist:{artist}".format(**album)
    response = spotify_api.search(query, offset=0, type="album")

    try:
        for _album in response.get("albums").get("items"):
            album = SpotifyAlbum(_album)
            print("Adding [{}] by [{}]".format(album.name, album.main_artist))
            return album.id
    except:
        return None


def get_spotify_albums(album_ids, spotify_api):
    MAX_ALBUM_IDS = 20
    chunked_album_ids = [
        album_ids[i : i + MAX_ALBUM_IDS] for i in range(0, len(album_ids), MAX_ALBUM_IDS)
    ]
    albums_list = []
    for albums in chunked_album_ids:
        print("Fetching tracks for [{}] albums".format(len(albums)))
        response = spotify_api.albums(albums)
        albums_list = albums_list + [SpotifyAlbum(album) for album in response.get("albums")]

    return albums_list


def get_track_ids(albums):
    tracks = []
    for album in albums:
        tracks = tracks + album.track_uris

    return tracks


MONTHS = [
    None,
    "January",
    "February",
    "March",
    "April",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    load_dotenv()
    print(
        "Welcome! We are going to setup spotify now, you will be redirected to log into your account"
    )

    print("Once that is done, copy the url you were redirected to and paste here")
    spotify_api = setup_spotify()
    current_user = spotify_api.me()
    month = input("Enter the month you want to query (1..12): ")
    year = input("Enter the year your want to query: ")

    print("\nSearching albums on Metal Archives...")
    albums = get_released_albums(month=month, year=year)

    print("\nSearching albums on Spotify...")
    spotify_album_ids = [
        album_id
        for album_id in [get_spotify_album_id(album, spotify_api) for album in albums]
        if album_id is not None
    ]

    print("\nFetching more information about albums...")
    spotify_albums = get_spotify_albums(spotify_album_ids, spotify_api)

    print("\nOrganizing tracklist...")

    playlist_name = input("Enter the playlist name: ")

    spotify_playlist = spotify_api.user_playlist_create(
        current_user.get("id"),
        playlist_name,
        public=True,
        collaborative=False,
    )

    spotify_tracks = get_track_ids(spotify_albums)

    # maximum number of tracks that can be added per request
    max_tracks = 100
    for tracks in [
        spotify_tracks[i : i + max_tracks] for i in range(0, len(spotify_tracks), max_tracks)
    ]:
        spotify_api.playlist_add_items(spotify_playlist.get("id"), tracks)

    print("\nDone! Check your spotify account")


if __name__ == "__main__":
    main()
