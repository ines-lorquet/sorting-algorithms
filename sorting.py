from time import perf_counter
from random import randint

class Sorting:
    def __init__(self):
        pass

    def tri_insertion(self,list):
        for i in range(1, len(list)):
            val = list[i]
            j = i-1
            while j>=0 and list[j]>val:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = val
        return list


    def random_list(self,n):
        list = []
        for i in range(n):
            list.append(randint(1,n))
        return list

tri = Sorting()
