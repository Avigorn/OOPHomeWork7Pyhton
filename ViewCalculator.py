import logging


class ViewCalculator:

    def __init__(self, calculable_factory):
        self.calculableFactory = calculable_factory

    def run(self):
        digits = float(input("Введите первый аргумент: "))
        view_calculator = self.calculableFactory.create(digits)
        while True:
            operator = input("Введите команду (+, -, *, /) : ")
            match operator:
                case "+":
                    temp = float(input("Введите второй аргумент: "))
                    view_calculator.__add__(temp)
                case "-":
                    temp = float(input("Введите второй аргумент: "))
                    view_calculator.__sub__(temp)
                case "*":
                    temp = float(input("Введите второй аргумент: "))
                    view_calculator.__mul__(temp)
                case "/":
                    temp = float(input("Введите второй аргумент: "))
                    view_calculator.__truediv__(temp)
                case "=":
                    result = view_calculator.Result()
                    print(f'Вывод: {result}')
                    break
            operator = input("Считать дальше:Y/N ?")
            match operator:
                case _:
                    if not operator == "Y":
                        result = view_calculator.Result()
                        print(f'Вывод: {result}')
                    break


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")
