import metallum

def get_released_albums(**kwargs):
    albums = metallum.album_search(
        title='',
        strict=False,
        year_from=kwargs.get('year', 2021),
        year_to=kwargs.get('year', 2021),
        month_from=kwargs.get('month', 1),
        month_to=kwargs.get('month', 1),
        genre='melodic death metal',
        types=[1]
    )

    return [
        {
            'artist': album.band_name,
            'name': album.title,
            'genre': album._details[2],
            'date': album._details[3][-14:-4],
        } for album in albums
    ]
