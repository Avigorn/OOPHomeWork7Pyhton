class Operations:

    def __init__(self, digits):
        self.digits = digits

    def __add__(self, other):
        self.digits += other
        return self

    def __sub__(self, other):
        self.digits -= other
        return self

    def __mul__(self, other):
        self.digits *= other
        return self

    def __truediv__(self, other):
        self.digits /= (other != 0)
        return self

    def Result(self):
        return self.digits
