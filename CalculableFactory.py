from Operations import Operations


class CalculableFactory:
    def create(self, digits):
        return Operations(digits)
