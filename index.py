import metallum

def get_albums():
    albums = metallum.album_search(
        title='',
        strict=False,
        year_from=2021,
        year_to=2021,
        month_from=1,
        month_to=1,
        genre='melodic death metal',
        types=[1]
    )

    return [
        { 'artist': album.band_name, 'album': album.title } for album in albums
    ]
