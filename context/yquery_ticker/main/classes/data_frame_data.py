from pandas import DataFrame

from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.enums.data_frame import DataFrame as DF


class DataFrameData(TimeSeriesDataCollection):

    def get_column_values(self, df: DataFrame, column: DF): return df[column.__name__].astype(column.__type__)
            
    @classmethod
    def mockk(cls):
        return DataFrameData()
