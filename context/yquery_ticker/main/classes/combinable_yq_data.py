from context.yquery_ticker.main.classes.time_series_data_collection import TimeSeriesDataCollection
from context.yquery_ticker.main.classes.yahoo.balance_sheet_data import BalanceSheetData
from context.yquery_ticker.main.classes.yahoo.cash_flow_data import CashFlowData
from context.yquery_ticker.main.const import WRONG_TYPE_STRING
from context.yquery_ticker.main.enums.growth_criteria import GrowthCriteria
from context.yquery_ticker.main.utils.dict_key_enum import DictKey


class CombinableYQData(TimeSeriesDataCollection):
    def __init__(
            self,
            combination: DictKey,
            balance_sheet: BalanceSheetData,
            cash_flow: CashFlowData,
    ):
        self.combination = combination
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow

    def combine_process_and_evaluate_growth_criteria(self):
        result = []
        if self.combination == DictKey.BOOK_VALUE_AND_DIVIDENDS:
            for balance_sheet_entry in self.balance_sheet:
                cashDividendsPaid = self.cash_flow.get_entry_of(
                    as_of_date=balance_sheet_entry.asOfDate,
                    period_type=balance_sheet_entry.periodType
                )
                result.append(balance_sheet_entry.commonStockEquity + cashDividendsPaid)
            return self.passes_percentage_increase_requirements(
                percentages=self.calculate_percentage_increase_for_simple_list(
                    simple_list=result
                ),
                percentage_requirement=GrowthCriteria.BOOK_VALUE_AND_DIVIDENDS.__percentage_criteria__
            )
        else:
            raise TypeError(WRONG_TYPE_STRING.format(type=self.combination))
