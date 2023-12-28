import unittest

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import IncomeStatementDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData
from context.yquery_ticker.main.enums.quarter import Quarter


class test_time_series_data_collection(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_time_series_data_collection, self).__init__(*args, **kwargs)

    def test_is_invalid_comparison(self):
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=None,
            later=1
        ) is True
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=1,
            later=None
        ) is True
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=None,
            later=1.0
        ) is True
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=None,
            later=None
        ) is True
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier="one",
            later=1
        ) is True
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=1,
            later="one"
        ) is True
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=1,
            later=1
        ) is False
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=1,
            later=1.0
        ) is False
        assert TimeSeriesDataCollection._is_invalid_comparison(
            earlier=1.0,
            later=1.0
        ) is False


