class FirstFactorial(object):

    def __init__(self, number):
        self.number = number

    def get(self):
        result = self.number
        for i in range(1, self.number):
            result *= i

        return result

first_factorial = FirstFactorial(8)
print(first_factorial.get())