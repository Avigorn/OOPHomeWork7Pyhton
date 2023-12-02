class Operations:

    def __init__(self, digits):
        """
        Метод инициации класса содержащий переменную числа
        :param digits:
        """
        self.digits = digits

    def __add__(self, other):
        """
        Метод сложения
        :param other: второе число в выражении
        :return:
        """
        self.digits += other
        return self

    def __sub__(self, other):
        """
        Метод вычитания
        :param other: второе число в выражении
        :return:
        """
        self.digits -= other
        return self

    def __mul__(self, other):
        """
        Метод умножения
        :param other: второе число в выражении
        :return:
        """
        self.digits *= other
        return self

    def __truediv__(self, other):
        """
        Метод деления
        :param other: второе число в выражении
        :return:
        """
        self.digits /= (other != 0)
        return self

    def Result(self):
        """
        Метод получения вывода математической операции
        :return:
        """
        return self.digits
