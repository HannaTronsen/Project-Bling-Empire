from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.charts import QuarterlyEarningsDataChart, QuarterlyFinancialsDataChart, YearlyFinancialsDataChart


class HistoricalEarnings(TimeSeriesDataCollection):

    quarterlyEarningsDataChart: list[QuarterlyEarningsDataChart]
    quarterlyFinancialsDataChart: list[QuarterlyFinancialsDataChart]
    yearlyFinancialsDataChart: list[YearlyFinancialsDataChart]
