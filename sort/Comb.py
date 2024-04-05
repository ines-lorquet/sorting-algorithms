import math  


class Comb:
    def __init__(self, array):
        self.array = array

    def comb_sort(self, array):
        permutation = True
        gap = len(array)
        while (permutation == True) or  (gap>1):
            permutation = False
            gap = math.floor(gap / 1.3)
            if gap<1: gap = 1
            for current in range(0, len(array) - gap):
                if array[current] > array[current + gap]:
                    permutation = True
                    # On echange les deux elements
                    array[current], array[current + gap] = \
                    array[current + gap],array[current]

        return self.array 