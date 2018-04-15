class Goldbach(object):

    # Todo: Implement the sieve algorithm.
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    def is_prime_number(self, number):
        skip = [0, 1, number]

        for i in range(number):
            if i in skip:
                continue

            if number % i == 0:
                return False

        return True

    def get_prime_numbers(self, number):
        prime_numbers = []
        for i in range(number):
            if self.is_prime_number(i):
                prime_numbers.append(i)

        return prime_numbers

    def calculate(self, number):
        skip = [0, 1]

        # Todo: weird stuff happening here, fix this.
        prime_numbers = self.get_prime_numbers(number)
        for i in self.get_prime_numbers(number):
            if i in skip:
                prime_numbers.remove(i)

        for i in prime_numbers:
            for j in prime_numbers:
                for k in prime_numbers:
                    if i + j + k == number:
                        print(str(number) + " = " + str(i) + " + " + str(j) + " + " + str(k))
                        return

        print('Impossible')

    def calculate_multiple(self, numbers):
        for i in numbers:
            self.calculate(i)


goldbach = Goldbach()
goldbach.calculate_multiple([111, 17, 199, 287, 53])