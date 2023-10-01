from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData

NET_INCOME = 'NetIncome'
TOTAL_REVENUE = 'TotalRevenue'


@dataclass
class IncomeStatementDataClass(YQDataFrameData):
    netIncome: Optional[float]
    totalRevenue: Optional[float]
