import csv
from enum import Enum
from typing import Callable
from const import GENERATED_CSV_FILES_PATH
from context.yquery_ticker.main.data_classes.financial_summary import FinancialSummary
from context.yquery_ticker.main.data_classes.general_stock_info import GeneralStockInfo
from context.yquery_ticker.main.errors.generic_error import GenericError


class Section(Enum):
    GENERAL_STOCK_INFO = "GENERAL STOCK INFO"
    REVENUE = "REVENUE"
    EARNINGS = "EARNINGS"
    DEBT = "DEBT"
    MARGINS = "MARGINS"
    DIVIDEND = "DIVIDEND"
    FINANCIAL_RATIO = "FINANCIAL RATIO"
    CASH_FLOW = "CASH FLOW"
    PROFITABILITY = "PROFITABILITY"
    GROWTH_CRITERIA = "PASSES GROWTH CRITERIA"


class CsvConverter:

    @staticmethod
    def _to_csv(
            ticker_symbol: str,
            general_stock_info: GeneralStockInfo,
            revenue_data: Callable[[], dict],
            earnings_data: Callable[[], dict],
            debt_data: Callable[[], dict],
            margins_data: Callable[[], dict],
            dividends_data: Callable[[], dict],
            financial_ratio_data: Callable[[], dict],
            cash_flow_data: Callable[[], dict],
            profitability_data: Callable[[], dict],
            evaluated_growth_criteria: Callable[[], dict],
            criteria_pass_count: int,
    ):
        mapped_data = {
            Section.REVENUE: revenue_data,
            Section.EARNINGS: earnings_data,
            Section.DEBT: debt_data,
            Section.MARGINS: margins_data,
            Section.DIVIDEND: dividends_data,
            Section.FINANCIAL_RATIO: financial_ratio_data,
            Section.CASH_FLOW: cash_flow_data,
            Section.PROFITABILITY: profitability_data,
            Section.GROWTH_CRITERIA: evaluated_growth_criteria,
        }

        with open(f"{GENERATED_CSV_FILES_PATH}/{ticker_symbol}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write general stock information section
            writer.writerow([Section.GENERAL_STOCK_INFO.value])
            for key, value in general_stock_info:
                if not isinstance(value, FinancialSummary) and value is not None and key != "long_business_summary":
                    writer.writerow([key.capitalize(), value])
                else:
                    if value is None:
                        writer.writerow([key.capitalize(), "None"])
            writer.writerow([])

            # Write each section
            for section, data_func in mapped_data.items():
                if section == Section.GROWTH_CRITERIA:
                    writer.writerows([[], []])

                writer.writerow([section.value])  # Write section header

                for key, value in data_func().items():
                    if not isinstance(value, GenericError) and value is not None:
                        writer.writerow([key, value])
                    else:
                        if value is None:
                            writer.writerow([key, "None"])
                        else:
                            error = GenericError(value.reason)
                            writer.writerow([key, error.reason])
                writer.writerow([])
            writer.writerows([[], []])
            writer.writerow(["CRITERIA PASS COUNT", criteria_pass_count])
        file.close()
