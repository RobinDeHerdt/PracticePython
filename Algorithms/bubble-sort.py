class BubbleSort(object):

    def __init__(self, list):
        self.list = list

    def execute(self):
        sorted = False
        while not sorted:
            sorted = True
            for key, value in enumerate(self.list):
                next_key = key + 1

                # Don't try to compare when we're on the last index.
                if len(self.list) <= next_key:
                    continue

                next_value = self.list[next_key]

                if value > next_value:
                    self.list[key] = next_value
                    self.list[next_key] = value
                    sorted = False

                print('Iterating: ' + str(self.list))

        print('Sorted list:' + str(self.list))

bubble_sort = BubbleSort([9, 5 ,8 ,3 ,4 ,17 ,11 ,22 ,0 ,1 ,3])
bubble_sort.execute()