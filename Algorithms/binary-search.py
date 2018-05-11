class BinarySearch(object):

    def __init__(self, needle, haystack):
        self.needle = needle
        self.haystack = haystack

    def execute(self):
        if not len(self.haystack):
            return print("Couldn't find number " + str(self.needle))

        lower_bound = 0
        upper_bound = len(self.haystack)
        while lower_bound < upper_bound:
            middle = (lower_bound + upper_bound) // 2
            if self.haystack[middle] < self.needle:
                lower_bound = middle + 1
            else:
                upper_bound = middle

        self.print_result(lower_bound)

    def print_result(self, index):
        if index >= len(self.haystack):
            print("Out of range")
        elif self.needle == self.haystack[index]:
            print("Found %s at index %s" % (self.haystack[index], index))
        else:
            print("Closest number I could find is %s at index %s" % (self.haystack[index], index))


binary_search = BinarySearch(4, [1, 2, 3, 4, 5, 6, 7, 8, 9])
binary_search.execute()
