import datetime
import re
from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.const import QUARTER_REGEX, QUARTER_YEAR_REGEX, YEAR_REGEX
from context.yquery_ticker.main.data_classes.charts import Date, QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart
from context.yquery_ticker.main.enums.quarter import Quarter


class HistoricalEarnings(TimeSeriesDataCollection):

    quarterlyEarningsDataChart: list[QuarterlyEarningsDataChart]
    quarterlyFinancialsDataChart: list[QuarterlyFinancialsDataChart]
    yearlyFinancialsDataChart: list[YearlyFinancialsDataChart]

    @classmethod
    def convert_date(self, value) -> Date:

        if value is None or value == "" or value == "N/A":
            return None

        is_valid_year_int = (
            type(value) != str
            and type(value) != float
            and value >= 0
        )
        if (is_valid_year_int):
            return Date(year=value)

        elif (type(value) == str):

            quarter_and_year = re.search(
                QUARTER_YEAR_REGEX, value, re.IGNORECASE)
            if quarter_and_year:
                quarter_date = str(quarter_and_year.group(1)).upper()
                year = int(quarter_and_year.group(2))
                return Date(year=year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))

            only_year = re.search(YEAR_REGEX, value)
            if only_year:
                year = int(only_year.group())
                return Date(year=year)

            only_quarter = re.search(QUARTER_REGEX, value, re.IGNORECASE)
            if only_quarter:
                quarter_date = str(only_quarter.group()).upper()
                return Date(year=datetime.datetime.year, quarter=Quarter.from_quarter_date(quarter_date=quarter_date))

        return None
