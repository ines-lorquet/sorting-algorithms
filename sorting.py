from time import perf_counter
from random import randint
from TriInsertion import TriInsertin

class Sorting(TriInsertin):
    def __init__(self):
        TriInsertin.__init__(self)

    def random_list(self,n):
        list = []
        for i in range(n):
            list.append(randint(1,n))
        return list

    def test(self):
        print(f"""
    1 : Tri Insertion""")

        self.choice = input("Witch method : ")
        if self.choice == "1":
            self.choice = self.tri_insertion
            
        for i in range(4):
            size = 10**(i+1)
            list_insertion = self.random_list(size)

            if size == 10:
                print()
                print(list_insertion,"Unordered List")
                print(self.choice(list_insertion), "Sorted List")
                print()
                
            debut_insertion = perf_counter()
            list_insertion = self.choice(list_insertion)
            fin_insertion= perf_counter()
            print(
                f"Tri sélection taille {str(size)} : {str(fin_insertion - debut_insertion)}"
            )
        print()
        
tri = Sorting()
tri.test()

