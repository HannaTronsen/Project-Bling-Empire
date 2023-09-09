from enum import Enum, auto

from ..classes.time_series_data_collection import TimeSeriesDataCollection


class YQDateFrameType(Enum):
    EarningsHistory = auto()


class YQDataFrameData(TimeSeriesDataCollection):

    def __init__(self, yq_data_frame_type: YQDateFrameType):
        self.yq_data_frame_type = yq_data_frame_type

    # @staticmethod
    # def get_column_values(df: DataFrame, column: DF): return df[column.__name__].astype(column.__type__)

    @classmethod
    def mockk(cls):
        return YQDataFrameData(yq_data_frame_type=YQDateFrameType.EarningsHistory)
