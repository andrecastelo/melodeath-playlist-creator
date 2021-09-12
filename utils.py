def get_years(arg):
    year = arg.get("year", 2021)
    year_from = arg.get("year_from", year)
    year_to = arg.get("year_to", year)

    return (
        year_from,
        year_to,
    )


def get_months(arg):
    month = arg.get("month", 1)
    month_from = arg.get("month_from", month)
    month_to = arg.get("month_to", month)

    return (
        month_from,
        month_to,
    )
