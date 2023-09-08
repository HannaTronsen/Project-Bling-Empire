import re
from dataclasses import dataclass
from typing import Any, Optional
from ..const import (
    QUARTER_REGEX,
    QUARTER_YEAR_REGEX,
    TIME_STAMP_REGEX,
    YEAR_REGEX
)
from ..enums.quarter import Month, Quarter


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
        match = re.search(f'^{YEAR_REGEX}$', date)
        if match:
            year = int(match.group())
            return Date(year=year)
        return None

    @classmethod
    def is_valid_quarter_only(cls, date: str):
        match = re.search(f'^{QUARTER_REGEX}$', date, re.IGNORECASE)
        if match:
            quarter_date = str(match.group()).upper()
            return Date(quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @classmethod
    def is_valid_quarter_and_year(cls, date):
        match = re.search(QUARTER_YEAR_REGEX, date, re.IGNORECASE)
        if match:
            quarter_date = str(match.group(1)).upper()
            year = int(match.group(2))
            return Date(year=year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @classmethod
    def is_valid_time_stamp(cls, date: str):
        # TODO (Hanna): Account for leap years / days
        match = re.search(TIME_STAMP_REGEX, date, re.IGNORECASE)
        if match:
            year = int(match.group(1))
            month = str(match.group(2))
            return Date(year=year, quarter=Month.from_month(month).__quarter__)
        return None

    @classmethod
    def convert_date(cls, date_input):
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

                elif cls.is_valid_time_stamp(date_input) is not None:
                    return cls.is_valid_time_stamp(date_input)
        return None
