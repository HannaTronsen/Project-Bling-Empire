"""
    This 'CastableDataInterface' makes it possible to check if it is possible to
    cast values when needed. It is handy if we use data that don't entirely conform to the class types
    from a JSON object to populate the class fields.
      
    If a class field takes a 'float' and a JSON object provides a an 'int', by casting it to the 
    correct type, we might avoid unexpected bugs related to wrong types when executing the software.

    If the value is not castable, it will return None
"""
from context.yquery_ticker.main.const import CASTABLE_ERROR_STRING, NO_CASTABLE_DEFINITION_ERROR_STRING

SHOW_PRINT = False


class CastableDataInterface:

    @staticmethod
    def _cast(field_type_name, value, cast):
        try:
            return cast(value)
        except (ValueError, TypeError) as e:
            if SHOW_PRINT:
                print(f'_cast threw an exception: {e}')
                print(CASTABLE_ERROR_STRING.format(value=value, field_type=field_type_name))

    def try_to_cast(self, field_type_name, value):
        casting_value = None
        if field_type_name == "float":
            casting_value = self._cast(field_type_name=field_type_name, value=value, cast=float)
        elif field_type_name == 'int':
            casting_value = self._cast(field_type_name=field_type_name, value=value, cast=int)
        elif field_type_name == 'str':
            casting_value = self._cast(field_type_name=field_type_name, value=value, cast=str)
        else:
            if SHOW_PRINT:
                print(NO_CASTABLE_DEFINITION_ERROR_STRING.format(field_type=field_type_name))

        return casting_value
