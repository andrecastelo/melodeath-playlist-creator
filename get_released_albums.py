import metallum
from utils import get_months, get_years


def assemble_params(params):
    year_from, year_to = get_years(params)
    month_from, month_to = get_months(params)

    return dict(
        title="",
        strict=False,
        year_from=year_from,
        year_to=year_to,
        month_from=month_from,
        month_to=month_to,
        genre="melodic death metal",
        types=[1],
    )


def get_released_albums(**kwargs):
    params = assemble_params(kwargs)
    albums = metallum.album_search(**params)

    return [
        {
            "artist": album.band_name,
            "name": album.title,
            "genre": album._details[2],
            "date": album._details[3][-14:-4],
        }
        for album in albums
    ]
