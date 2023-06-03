import re
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any
from context.yquery_ticker.main.const import QUARTER_REGEX, QUARTER_YEAR_REGEX, YEAR_REGEX
from context.yquery_ticker.main.enums.quarter import Quarter
import datetime
from context.yquery_ticker.main.utils.dict_key_enum import DictKey


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
class Chart(ABC):
    date: Date

    def convert_date(self): 
        self.date = Date.convert_date(value=self.date)
        return self
    
    @abstractmethod
    def get_section_from_json_path(self):
        pass
    

@dataclass
class QuarterlyEarningsDataChart(Chart):
    actual: float
    estimate: float #just to map to model for now
    
    def get_section_from_json_path(base): return base ['earningsChart'] ['quarterly']
    

@dataclass
class FinancialsDataChart(Chart):
    revenue: float
    earnings: float
    
@dataclass
class QuarterlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(base): return base ['financialsChart'] ['quarterly']

@dataclass
class YearlyFinancialsDataChart(FinancialsDataChart):
    def get_section_from_json_path(base): return base ['financialsChart'] ['yearly']
    
