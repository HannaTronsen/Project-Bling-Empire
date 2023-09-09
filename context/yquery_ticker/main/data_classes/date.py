import re
from dataclasses import dataclass
from typing import Any, Optional

from ..enums.country import Country
from ..enums.quarter import Month, Quarter


class TimeRegex:
    YEAR_REGEX = r"(\d{4})"
    QUARTER_REGEX = r"([1-4]Q)"
    MONTH_REGEX = r"(0[1-9]|1[0-2])"
    DAY_REGEX = r"(0[1-9]|1\d|2\d|3[01])"
    QUARTER_YEAR_REGEX = fr"^{QUARTER_REGEX}{YEAR_REGEX}$"

    US_DATE_TIME_TIME_REGEX = fr"^{YEAR_REGEX}-{MONTH_REGEX}-{DAY_REGEX}$"
    NO_DATE_TIME_TIME_REGEX = fr"^{DAY_REGEX}-{MONTH_REGEX}-{YEAR_REGEX}$"


@dataclass
class Date:
    year: Optional[int] = None
    quarter: Optional[Quarter] = None

    @classmethod
    def is_valid_year(cls, date: Any) -> bool:
        return (
                type(date) != str
                and type(date) != float
                and date >= 0
        )

    @classmethod
    def is_valid_year_only(cls, date: str):
        match = re.search(f'^{TimeRegex.YEAR_REGEX}$', date)
        if match:
            year = int(match.group())
            return Date(year=year)
        return None

    @classmethod
    def is_valid_quarter_only(cls, date: str):
        match = re.search(f'^{TimeRegex.QUARTER_REGEX}$', date, re.IGNORECASE)
        if match:
            quarter_date = str(match.group()).upper()
            return Date(quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @classmethod
    def is_valid_quarter_and_year(cls, date):
        match = re.search(TimeRegex.QUARTER_YEAR_REGEX, date, re.IGNORECASE)
        if match:
            quarter_date = str(match.group(1)).upper()
            year = int(match.group(2))
            return Date(year=year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @staticmethod
    def _get_correct_date_time_regex(date, date_time_format):
        if date_time_format is None:
            # Default
            return re.search(TimeRegex.US_DATE_TIME_TIME_REGEX, date, re.IGNORECASE)
        if date_time_format == Country.NO:
            return re.search(TimeRegex.NO_DATE_TIME_TIME_REGEX, date, re.IGNORECASE)

    @classmethod
    def is_valid_date_time(cls, date: str, date_time_format: Country):
        # TODO (Hanna): Account for leap years / days
        match = cls._get_correct_date_time_regex(date=date, date_time_format=date_time_format)
        if match:
            year = int(match.group(1))
            month = str(match.group(2))
            return Date(year=year, quarter=Month.from_month(month).__quarter__)
        return None

    @classmethod
    def convert_date(cls, date_input, date_time_format: Country = None):
        valid_date_input = date_input is not None and date_input != "" and date_input != "N/A"
        if valid_date_input:
            if cls.is_valid_year(date=date_input):
                return Date(year=date_input)
            elif type(date_input) == str:
                if cls.is_valid_quarter_and_year(date_input) is not None:
                    return cls.is_valid_quarter_and_year(date_input)

                elif cls.is_valid_year_only(date_input) is not None:
                    return cls.is_valid_year_only(date_input)

                elif cls.is_valid_quarter_only(date_input) is not None:
                    return cls.is_valid_quarter_only(date_input)

                elif cls.is_valid_date_time(date_input, date_time_format) is not None:
                    return cls.is_valid_date_time(date_input, date_time_format)
        return None
