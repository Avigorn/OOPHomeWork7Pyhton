from CalculableFactory import CalculableFactory
from ViewCalculator import ViewCalculator


class Main:

    def __init__(self):
        self.calculable_factory = CalculableFactory()
        self.view = ViewCalculator(self.calculable_factory)
        self.view.run()


main = Main()
main.__init__()

