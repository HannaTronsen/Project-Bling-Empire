class GenericError:
    def __init__(self, reason: str):
        self.reason = reason

    def reason(self):
        print(self.reason)
