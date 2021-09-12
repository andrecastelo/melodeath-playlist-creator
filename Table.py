class Table:
    def __init__(self, albums):
        self.albums = albums

    def markdown(self):
        headers = [
            "Band | Followers | Album | Genre | Date | Playlist",
            ":----|:----------|:------|:------|-----:|:--------",
        ]
        lines = [Table.format(album) for album in self.albums]

        return headers + lines

    def print_markdown(self):
        print("\n".join(self.markdown()))

    @staticmethod
    def format(album):
        spotify_album = album.get("spotify_album")

        if spotify_album:
            return "{artist} | {followers} | {name} | {genre} | {date} | {playlist}".format(
                artist=spotify_album.main_artist.get("name"),
                followers=spotify_album.followers if spotify_album.followers else "-",
                name=spotify_album.name,
                genre=album.get("genre", "-"),
                date=spotify_album.release_date,
                playlist=spotify_album.external_url,
            )

        return "{artist} | - | {name} | {genre} | {date} | -".format(**album)
