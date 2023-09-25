from dataclasses import dataclass
from typing import Optional
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData

COMMON_STOCK_EQUITY = 'CommonStockEquity'


@dataclass
class BalanceSheetDataClass(YQDataFrameData):
    commonStockEquity: Optional[float]
