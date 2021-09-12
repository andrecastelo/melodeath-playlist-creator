import metallum
from utils import get_months, get_years
from datetime import date


def assemble_params(**kwargs):
    year_from, year_to = get_years(kwargs)
    month_from, month_to = get_months(kwargs)
    today = date.today()

    if year_to > today.year:
        year_to = today.year

    if month_to > today.month:
        month_to = today.month - 1

    return dict(
        title="",
        strict=False,
        year_from=year_from,
        year_to=year_to,
        month_from=month_from,
        month_to=month_to,
        genre="melodic death metal",
        types=[1],
        page_start=kwargs.get("page_start", 0),
    )


def get_released_albums(**kwargs):
    params = assemble_params(**kwargs)
    albums = metallum.album_search(**params)
    result_count = albums.result_count
    PAGE_LENGTH = 200

    while len(albums) < result_count:
        params["page_start"] += PAGE_LENGTH
        new_search = metallum.album_search(**params)
        albums += new_search

    return [
        {
            "artist": album.band_name,
            "name": album.title,
            "genre": album._details[2],
            "date": album._details[3][-14:-4],
        }
        for album in albums
    ]
