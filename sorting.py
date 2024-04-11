from time import perf_counter
from random import randint

class Sorting:
    def __init__(self):
        pass

    def tri_selection(self,list):
        for i in range(len(list)-1):
            i_min = i
            for j in range(i+1, len(list)):
                if list[j]<list[i_min]:
                    i_min=j
            list[i],list[i_min]=list[i_min],list[i]
        return list

    def random_list(self,n):
        list = []
        for i in range(n):
            list.append(randint(1,n))
        return list

tri = Sorting()
for i in range(4):
    size = 10**(i+1)
    list_selection = tri.random_list(size)

    if size == 10:
        print()
        print(list_selection,"Unordered List")
        print(tri.tri_selection(list_selection), "Sorted List")
        print()
        
    if i < 4:
        debut_selection = perf_counter()
        list_selection = tri.tri_selection(list_selection)
        fin_selection = perf_counter()
        print(
            f"Tri sélection taille {str(size)} : {str(fin_selection - debut_selection)}"
        )
    print()