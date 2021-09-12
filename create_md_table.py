from dotenv import load_dotenv
from typing import Optional
import typer

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


start_date_help = "Starting date to query, format MM/YYYY"
end_date_help = "End date, format MM/YYYY"


def main(
    start_date: str = typer.Argument(..., help=start_date_help),
    end_date: Optional[str] = typer.Argument(None, help=end_date_help),
):
    month_from, year_from = start_date.split("/")
    month_to, year_to = (
        end_date.split("/")
        if end_date
        else (
            month_from,
            year_from,
        )
    )

    typer.echo(f"Period: between {month_from}-{year_from} and {month_to}-{year_to}")
    typer.echo("Fetching released albums for the period on Metal Archives...")
    albums = get_released_albums(
        month_from=month_from, month_to=month_to, year_from=year_from, year_to=year_to
    )
    typer.echo(f"Found [{len(albums)}] albums on Metal Archives")

    typer.echo("Setting up Spotify API...")
    load_dotenv()
    spotify_api = setup_spotify()

    typer.echo("Fetching album data on Spotify...")
    with typer.progressbar(albums) as progress:
        for album in progress:
            spotify_album = search_album(album, spotify_api)
            if spotify_album:
                album["spotify_album"] = spotify_album

    markdown_table = Table(albums)
    markdown_table.print_markdown()


if __name__ == "__main__":
    typer.run(main)
