# {'album_type': 'album',
#   'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5JO1ShiUsRZ2emtk2uRecI'},
#     'href': 'https://api.spotify.com/v1/artists/5JO1ShiUsRZ2emtk2uRecI',
#     'id': '5JO1ShiUsRZ2emtk2uRecI',
#     'name': 'Aztlan',
#     'type': 'artist',
#     'uri': 'spotify:artist:5JO1ShiUsRZ2emtk2uRecI'}],
#   'available_markets': [],
#   'external_urls': {'spotify': 'https://open.spotify.com/album/0pCjmh3QzbF98tuyXHcAIK'},
#   'href': 'https://api.spotify.com/v1/albums/0pCjmh3QzbF98tuyXHcAIK',
#   'id': '0pCjmh3QzbF98tuyXHcAIK',
#
#   'name': 'Legion Mexica',
#   'release_date': '2021-01-06',
#   'release_date_precision': 'day',
#   'total_tracks': 9,
#   'type': 'album',
#   'uri': 'spotify:album:0pCjmh3QzbF98tuyXHcAIK'}


class SpotifyAlbum:
    def __init__(self, details):
        self.artists = details.get("artists")
        self.main_artist = None
        self.main_artist_uri = self.artists[0].get("uri")
        self.name = details.get("name")
        self.release_date = details.get("release_date")
        self.external_url = details.get("external_urls", {}).get("spotify")
        self.total_tracks = details.get("total_tracks")
        self.id = details.get("id")
        self.uri = details.get("uri")
        self.tracks = [
            {
                "id": track.get("id"),
                "uri": track.get("uri"),
                "track_number": track.get("track_number"),
                "name": track.get("name"),
            }
            for track in details.get("tracks", {}).get("items", [])
        ]

    @property
    def followers(self):
        if self.main_artist:
            return self.main_artist.get("followers").get("total")

        return None

    @property
    def track_ids(self):
        return [track.get("id") for track in self.tracks if track.get("id") is not None]

    @property
    def track_uris(self):
        return [
            track.get("uri") for track in self.tracks if track.get("id") is not None
        ]

    def __len__(self):
        return self.total_tracks

    def __repr__(self):
        return "{}<{}, {}>".format(
            self.__class__.__name__,
            self.name,
            self.main_artist,
        )
