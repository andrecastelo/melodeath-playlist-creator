from datetime import datetime
from utils import parse_big_number

sort_lambda = lambda album: datetime.strptime(album.get("date"), "%Y-%m-%d")


class Table:
    def __init__(self, albums):
        self.albums = sorted(albums, key=sort_lambda)

    def markdown(self):
        headers = [
            "     | Band | Followers | Album | Genre | Playlist",
            "|---:|:-----|----------:|:------|:------|:--------",
        ]
        lines = [Table.format(album) for album in self.albums]

        return headers + lines

    def print_markdown(self):
        print("\n".join(self.markdown()))

    @staticmethod
    def format_date(date, format="%b %d"):
        return datetime.strptime(date, "%Y-%m-%d").strftime(format)

    @staticmethod
    def format(album):
        spotify_album = album.get("spotify_album")

        if spotify_album:
            follower_count = (
                parse_big_number(spotify_album.followers)
                if spotify_album.followers
                else "-"
            )

            return "{date} | {artist} | {followers} | {name} | {genre} | [link]({playlist})".format(
                date=Table.format_date(spotify_album.release_date),
                artist=spotify_album.main_artist.get("name"),
                followers=follower_count,
                name=spotify_album.name,
                genre=album.get("genre", "-"),
                playlist=spotify_album.external_url,
            )

        return "{date} | {artist} | - | {name} | {genre} | -".format(
            date=Table.format_date(album.get("date")),
            artist=album.get("artist"),
            name=album.get("name"),
            genre=album.get("genre"),
        )
