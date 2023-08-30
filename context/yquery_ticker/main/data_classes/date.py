import re
from dataclasses import dataclass
from typing import Any
from context.yquery_ticker.main.const import QUARTER_REGEX, QUARTER_YEAR_REGEX, TIME_STAMP_REGEX, YEAR_REGEX
from context.yquery_ticker.main.enums.quarter import Month, Quarter
import datetime


@dataclass
class Date:
    year: int
    quarter: Quarter = None

    @classmethod
    def is_valid_year(cls, value: Any) -> bool:
        return (
            type(value) != str
            and type(value) != float
            and value >= 0
        )

    @classmethod
    def is_valid_year_only(cls, value: str):
        match = re.search(f'^{YEAR_REGEX}$', value)
        if match:
            year = int(match.group())
            return Date(year=year)
        return None

    @classmethod
    def is_valid_quarter_only(cls, value: str):
        match = re.search(f'^{QUARTER_REGEX}$', value, re.IGNORECASE)
        if match:
            quarter_date = str(match.group()).upper()
            return Date(year=datetime.datetime.year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @classmethod
    def is_valid_quarter_and_year(cls, value):
        match = re.search(QUARTER_YEAR_REGEX, value, re.IGNORECASE)
        if match:
            quarter_date = str(match.group(1)).upper()
            year = int(match.group(2))
            return Date(year=year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @classmethod
    def is_valid_time_stamp(cls, value: str):
        match = re.search(TIME_STAMP_REGEX, value, re.IGNORECASE)
        if match:
            year = int(match.group(1))
            month = str(match.group(2))
            return Date(year=year, quarter=Month.from_month(month).__quarter__)
        return None

    @classmethod
    def convert_date(cls, value):
        date = None
        if value is not None and value != "" and value != "N/A":
            if cls.is_valid_year(value=value):
                return Date(year=value)
            elif type(value) == str:
                if cls.is_valid_quarter_and_year(value) is not None:
                    date = cls.is_valid_quarter_and_year(value)
                elif cls.is_valid_year_only(value) is not None:
                    date = cls.is_valid_year_only(value)
                elif cls.is_valid_quarter_only(value) is not None:
                    date = cls.is_valid_quarter_only(value)
                elif cls.is_valid_time_stamp(value) is not None:
                    date = cls.is_valid_time_stamp(value)
        return date
