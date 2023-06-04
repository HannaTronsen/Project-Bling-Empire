from context.yquery_ticker.main.enums.cash_flow_type import CashFlowType

RELATIVE_PATH = 'context/yquery_ticker'
YQUERY_TEST_PATH = f'{RELATIVE_PATH}/tests/'
DEFAULT_CASH_FLOW_METRIC = CashFlowType.FREE_CASH_FLOW

QUARTER_YEAR_REGEX = r"([1-4]Q)(\d{4})"
YEAR_REGEX = r"^(\d{4})$"
QUARTER_REGEX = r"^([1-4]Q)$"

ATTRIBUTE_ERROR_STRING = "Failed to retrieve attribute '{attribute}' from chart at index {index}"
WRONG_TYPE_STRING = "Wrong type: {type}."
INVALID_LIST_LENGTH_STRING = "List of values is either empty or too small: {chart_list}."
INVALID_FIELD_STRING = '\n {field} has invalid or null value and will be handled.'
NO_CASTABLE_DEFINITION_ERROR_STRING = "{field_type} don't have a castable definition yet. Implemented it in 'CastableDataInterface'."
CASTABLE_ERROR_STRING = "Casting failed. The value: '{value}' is not convertible to '{field_type}'."
