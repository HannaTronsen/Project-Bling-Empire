from context.yquery_ticker.main.enums.cash_flow_type import CashFlowType

RELATIVE_PATH = 'context/yquery_ticker'
YQUERY_TEST_PATH = f'{RELATIVE_PATH}/tests/'
DEFAULT_CASH_FLOW_METRIC = CashFlowType.FREE_CASH_FLOW

INVALID_FIELD_STRING = '\n {%$FIELD%} has invalid or null value and will be handled.'
NO_CASTABLE_DEFINITION_ERROR_STRING = "{%$FIELD_TYPE%} don't have a castable definition yet. Implemented it in 'CastableDataInterface'."
CASTABLE_ERROR_STRING = "Casting failed. The value: '{%$VALUE%}' is not convertible to '{%$FIELD_TYPE%}'."