import unittest

from context.yquery_ticker.main.data_classes.date import Date, PeriodType
from context.yquery_ticker.main.data_classes.yq_data_frame_data.income_statement import IncomeStatementDataClass
from context.yquery_ticker.main.data_classes.yq_data_frame_data.yq_data_frame_data import YQDataFrameData
from context.yquery_ticker.main.enums.quarter import Quarter


class test_yq_data_frame(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_yq_data_frame, self).__init__(*args, **kwargs)

    def test_sorted_model_list(self):
        sorted_model_list_by_quarter = [
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2022,
                    quarter=Quarter.FIRST_QUARTER
                ),
                periodType=PeriodType.MONTH_12
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2022,
                    quarter=Quarter.SECOND_QUARTER
                ),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2022,
                    quarter=Quarter.THIRD_QUARTER
                ),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2022,
                    quarter=Quarter.FOURTH_QUARTER
                ),
                periodType=PeriodType.MONTH_12,
            ),
        ]
        assert YQDataFrameData.sorted(
            unsorted_model_list=[
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2022,
                        quarter=Quarter.SECOND_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                ),
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2022,
                        quarter=Quarter.FIRST_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                ),
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2022,
                        quarter=Quarter.FOURTH_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                ),
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2022,
                        quarter=Quarter.THIRD_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                ),
            ]
        ) == sorted_model_list_by_quarter

        sorted_model_list_by_year_and_quarter = [
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2019,
                    quarter=Quarter.FIRST_QUARTER
                ),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2021,
                    quarter=Quarter.SECOND_QUARTER
                ),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2023,
                    quarter=Quarter.THIRD_QUARTER
                ),
                periodType=PeriodType.MONTH_12,
            ),
            IncomeStatementDataClass.mockk(
                asOfDate=Date(
                    year=2024,
                    quarter=Quarter.FOURTH_QUARTER
                ),
                periodType=PeriodType.MONTH_12,
            ),
        ]
        assert YQDataFrameData.sorted(
            unsorted_model_list=[
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2021,
                        quarter=Quarter.SECOND_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                ),
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2024,
                        quarter=Quarter.FOURTH_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                ),
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2023,
                        quarter=Quarter.THIRD_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                ),
                IncomeStatementDataClass.mockk(
                    asOfDate=Date(
                        year=2019,
                        quarter=Quarter.FIRST_QUARTER
                    ),
                    periodType=PeriodType.MONTH_12,
                )
            ]
        ) == sorted_model_list_by_year_and_quarter
