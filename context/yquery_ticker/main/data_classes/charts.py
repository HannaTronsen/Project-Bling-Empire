import re
from dataclasses import dataclass
from typing import Any
from context.yquery_ticker.main.const import QUARTER_REGEX, QUARTER_YEAR_REGEX, YEAR_REGEX
from context.yquery_ticker.main.enums.quarter import Quarter
import datetime


@dataclass
class Date:
    year: int
    quarter: Quarter = None

    @classmethod
    def is_valid_year(self, value: Any) -> bool:
        return (
            type(value) != str
            and type(value) != float
            and value >= 0
        )

    @classmethod
    def is_valid_year_only(self, value: str):
        match = re.search(YEAR_REGEX, value)
        if (match):
            year = int(match.group())
            return Date(year=year)
        return None

    @classmethod
    def is_valid_quarter_only(self, value: str):
        match = re.search(QUARTER_REGEX, value, re.IGNORECASE)
        if (match):
            quarter_date = str(match.group()).upper()
            return Date(year=datetime.datetime.year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @classmethod
    def is_valid_quarter_and_year(self, value):
        match = re.search(QUARTER_YEAR_REGEX, value, re.IGNORECASE)
        if (match):
            quarter_date = str(match.group(1)).upper()
            year = int(match.group(2))
            return Date(year=year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))
        return None

    @classmethod
    def convert_date(self, value):
        date = None
        if value is not None and value != "" and value != "N/A":
            if (self.is_valid_year(value=value)):
                return Date(year=value)

            elif (type(value) == str):

                if self.is_valid_quarter_and_year(value) is not None:
                    date = self.is_valid_quarter_and_year(value)
                elif self.is_valid_year_only(value) is not None:
                    date = self.is_valid_year_only(value)
                elif self.is_valid_quarter_only(value) is not None:
                    date = self.is_valid_quarter_only(value)

        return date


@dataclass
class QuarterlyEarningsDataChart:
    date: Date
    actual: float


@dataclass
class QuarterlyFinancialsDataChart:
    date: Date
    revenue: float
    earnings: float


@dataclass
class YearlyFinancialsDataChart:
    date: Date
    revenue: float
    earnings: float
