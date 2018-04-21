class BinarySearch(object):

    # TODO: Improve performace by calculating bounds
    # TODO: Work out the correct way to slice the list
    def execute(self, needle, haystack):
        if not len(haystack):
            return print("Couldn't find number " + str(needle))

        index = len(haystack) // 2

        print(haystack)

        if needle == haystack[index]:
            print("Found number " + str(needle) + "!")
            return
        elif needle > haystack[index]:
            return self.execute(needle, haystack[index+1:])
        elif needle < haystack[index]:
            return self.execute(needle, haystack[:index-1])

binary_search = BinarySearch()
binary_search.execute(10, [1, 2, 3, 4, 5, 6, 7, 8, 9])
