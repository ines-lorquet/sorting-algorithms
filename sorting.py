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


for i in range(4):
    size = 10**(i+1)
    list_insertion = tri.random_list(size)

    if size == 10:
        print()
        print(list_insertion,"Unordered List")
        print(tri.tri_insertion(list_insertion), "Sorted List")
        print()
        
    debut_insertion = perf_counter()
    list_insertion = tri.tri_insertion(list_insertion)
    fin_insertion= perf_counter()
    print(
        f"Tri sélection taille {str(size)} : {str(fin_insertion - debut_insertion)}"
    )
print()