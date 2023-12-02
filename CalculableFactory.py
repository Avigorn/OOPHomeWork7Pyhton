from Operations import Operations


class CalculableFactory:
    def create(self, digits):
        """
        Метод создания базового числа
        :param digits: первый аргумент выражения
        :return:
        """
        return Operations(digits)
