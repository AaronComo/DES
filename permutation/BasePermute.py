class BasePermute:
    def __init__(self):
        self.TABLE = None

    def handle(self, group):
        assert self.TABLE is not None
        m = str()
        for i in self.TABLE:
            m += group[i]
        return m
