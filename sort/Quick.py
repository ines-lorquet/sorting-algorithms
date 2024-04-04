class Quick:
    def __init__(self, array):
        self.array = array 

    def quick_sort(self, array):

        if not array:
            return []
        else:
            pivot = array[-1]
            smallest = [x for x in array     if x <  pivot]
            biggest = [x for x in array[:-1] if x >= pivot]
            return self.quick_sort(smallest) + [pivot] + self.quick_sort(biggest)