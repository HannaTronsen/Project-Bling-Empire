class TestCase:
    def __init__(self, **kwargs):
        self.cash_flow = None
        self.price = None
        self.none_value = None
        self.attribute = None
        self.model_list = None
        self.series_input = None

        self.expected_bool = None
        self.expected_exception = None
        self.expected_interval = None
        self.expected_result = None
        self.__dict__.update(kwargs)
