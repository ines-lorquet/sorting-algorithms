import random
from TriSelection import TriSelection
from TriBulle import TriBulle
from TriInsertion import TriInsertion
from time import time


class CreateList:
    def __init__(self, length, min_value, max_value):
        self.length = length
        self.min_value = min_value
        self.max_value = max_value

    def generate_list(self):
        """
        Generates a list of random numbers.

        Returns:
            list: A list of random real numbers.
        """
        generated_list = [round(random.uniform(self.min_value, self.max_value), 1) for _ in range(self.length)]
        return generated_list


if __name__ == "__main__":

    length = int(input ("\nChoisissez une longueur de liste : "))
    min_value = 0.1
    max_value = 1000.0

    createList = CreateList(length, min_value, max_value)
    unordered_list = createList.generate_list()
    print(f"\nLa liste de {length} nombres réels à été générée.\n")

    # print ("Tri sélecion : \033[94m 1 \033[0m\nTri bulle : \033[94m 2 \033[0m\nTri insertion : \033[94m 3 \033[0m\n")


    for i in range(1,8):
        print(f"Tri {['sélection', 'bulle', 'insertion', 'fusion', 'rapide', 'par tas', 'à peigne'][i-1]} - \033[94m{i}\033[0m")

    sort = int(input("\nChoisissez le chiffre correspondant à la méthode de tri voulue : "))

    if sort == 1:
        triSelection = TriSelection (unordered_list)
        start_time = time()
        sorted_list = triSelection.selection_sort()
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")


    if sort == 2:
        triBulle = TriBulle (unordered_list)
        start_time = time() 
        sorted_list = triBulle.bubble_sort()
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")

    if sort == 3:
        triInsertion = TriInsertion (unordered_list)
        start_time = time()
        sorted_list = triInsertion.insertion_sort()
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")


