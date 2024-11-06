class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, numbers):
        return [n * self.factor for n in numbers]