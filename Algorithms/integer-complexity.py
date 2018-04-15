class IntegerComplexity(object):

    def __init__(self, number):
        self.number = number

    def calculate(self):
        smallest_total = self.number + 1
        for i in range(1, self.number + 1):
            if self.number % i == 0:
                quotient = int(self.number / i)
                if (quotient + i) < smallest_total:
                    smallest_total = (quotient + i)

        print(smallest_total)



IntegerComplexity(12).calculate()
IntegerComplexity(456).calculate()
IntegerComplexity(4567).calculate()
IntegerComplexity(12345).calculate()