import metallum


def get_released_albums(**kwargs):
    year = kwargs.get("year", 2021)
    year_from = kwargs.get("year_from", year)
    year_to = kwargs.get("year_to", year)

    month = kwargs.get("month", 1)
    month_from = kwargs.get("month_from", month)
    month_to = kwargs.get("month_to", month)

    albums = metallum.album_search(
        title="",
        strict=False,
        year_from=year_from,
        year_to=year_to,
        month_from=month_from,
        month_to=month_to,
        genre="melodic death metal",
        types=[1],
    )

    return [
        {
            "artist": album.band_name,
            "name": album.title,
            "genre": album._details[2],
            "date": album._details[3][-14:-4],
        }
        for album in albums
    ]
