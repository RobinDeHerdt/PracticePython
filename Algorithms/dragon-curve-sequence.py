class DragonCurveSequence(object):

    def __init__(self, iterations):
        self.iterations = iterations

    def solve(self, sequence, iteration=0):
        result_sequence = ""

        prev = sequence[0]
        for index, number in enumerate(sequence):
            result_sequence += prev
            if prev == "1":
                prev = "0"
            else:
                prev = "1"

            result_sequence += str(number)

        if iteration >= self.iterations:
            print(result_sequence)
            return

        iteration += 1

        self.solve(result_sequence, iteration)


DragonCurveSequence(8).solve("1")
