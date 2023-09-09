from .enums.cash_flow_type import CashFlowType

RELATIVE_PATH = 'context/yquery_ticker'
YQUERY_TEST_PATH = f'{RELATIVE_PATH}/tests/'
HISTORICAL_EARNINGS_TEST_PATH = f'{YQUERY_TEST_PATH}/historical_earnings/'
DEFAULT_CASH_FLOW_METRIC = CashFlowType.FREE_CASH_FLOW

ATTRIBUTE_ERROR_STRING = "Failed to retrieve attribute '{attribute}' from chart at index {index}"
WRONG_TYPE_STRING = "Wrong type: {type}."
INVALID_LIST_LENGTH_STRING = "List of values is either empty or too small: {list}."
INVALID_VALUE_COMPARISON = "Couldn't compare values. They could be 'None' type or not the same type. value1 type:{value1}, value2 type: {value2}"
INVALID_FIELD_STRING = '\n {field} has invalid or null value and will be handled.'
NO_CASTABLE_DEFINITION_ERROR_STRING = "{field_type} don't have a castable definition yet. Implemented it in 'CastableDataInterface'."
CASTABLE_ERROR_STRING = "Casting failed. The value: '{value}' is not convertible to '{field_type}'."
NO_MATCHING_ENUM_MEMBER_STRING = "No matching enum member found for {identifier}: {value}"
