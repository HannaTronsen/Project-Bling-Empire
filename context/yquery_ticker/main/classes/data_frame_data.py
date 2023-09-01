from pandas import DataFrame

from ..classes.time_series_data_collection import TimeSeriesDataCollection
from ..enums.data_frame import DataFrame as DF


class DataFrameData(TimeSeriesDataCollection):

    @staticmethod
    def get_column_values(df: DataFrame, column: DF): return df[column.__name__].astype(column.__type__)

    @classmethod
    def mockk(cls):
        return DataFrameData()
