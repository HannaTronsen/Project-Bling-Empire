from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.data_classes.date import Date
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData

EPS_ACTUAL = 'epsActual'
EPS_ESTIMATE = 'epsEstimate'
EPS_DIFFERENCE = 'epsDifference'
EPS_QUARTER = 'quarter'


@dataclass
class EarningsHistoryDataClass(YQDataFrameData):
    epsActual: Optional[float]
    epsEstimate: Optional[float]
    epsDifference: Optional[float]
    quarter: Date
