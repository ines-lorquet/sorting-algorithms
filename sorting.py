from time import perf_counter
from random import randint

class Sorting:
    def __init__(self):
        pass

    def tri_selection(self,tab):
        for i in range(len(tab)-1):
            i_min = i
            for j in range(i+1, len(tab)):
                if tab[j]<tab[i_min]:
                    i_min=j
            tab[i],tab[i_min]=tab[i_min],tab[i]
        return tab
    
    def random_tab(n):
        tab = []
        for i in range(n):
            tab.append(randint(1,n))
        return tab