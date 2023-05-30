from dataclasses import dataclass
from context.yquery_ticker.main.classes.castable_data import CastableDataInterface
from context.yquery_ticker.main.enums.quarter import Quarter

@dataclass
class Date(CastableDataInterface):
	year: int
	quarter: Quarter = None

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
    