def get_years(arg):
    year = arg.get("year", 2021)
    year_from = arg.get("year_from", year)
    year_to = arg.get("year_to", year)

    return (
        int(year_from),
        int(year_to),
    )


def get_months(arg):
    month = arg.get("month", 1)
    month_from = arg.get("month_from", month)
    month_to = arg.get("month_to", month)

    return (
        int(month_from),
        int(month_to),
    )


THOUSAND = 1e3
HUNDRED_THOUSAND = 1e5
MILLION = 1e6
TEN_MILLION = 1e7


def parse_big_number(number):
    if number < THOUSAND:
        return str(number)

    if number < HUNDRED_THOUSAND:
        return f"{(number // 100) / 10}K"

    if number < MILLION:
        return f"{number // 1000}K"

    if number < TEN_MILLION:
        return f"{(number // 100_000) / 10}M"

    return f"{number // 1_000_000}M"
