from datetime import date, timedelta
from typing import Generator


def daterange(start_date: date, end_date: date) -> Generator:
    """Iterate over dates.

    Args:
        start_date: date to start iteration.
        end_date: date to finish iteration.

    Returns:
        Generator with dates iteration.
    """
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
