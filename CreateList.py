import random
from sort.Selection import Selection
from sort.Bulle import Bulle
from sort.Insertion import Insertion
from sort.Fusion import Fusion
from sort.Quick import Quick
from sort.Heap import Heap
# from sort.Comb import Comb
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

    for i in range(1,8):
        print(f"Tri {['sélection', 'bulle', 'insertion', 'fusion', 'rapide', 'par tas', 'à peigne'][i-1]} - \033[94m{i}\033[0m")

    sort = int(input("\nChoisissez le chiffre correspondant à la méthode de tri voulue : "))

    if sort == 1:
        Selection = Selection (unordered_list)
        start_time = time()
        sorted_list = Selection.selection_sort()
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")

    if sort == 2:
        Bulle = Bulle (unordered_list)
        start_time = time() 
        sorted_list = Bulle.bubble_sort()
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")

    if sort == 3:
        Insertion = Insertion (unordered_list)
        start_time = time()
        sorted_list = Insertion.insertion_sort()
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")

    if sort == 4:
        Fusion = Fusion(unordered_list)  # Instantiate Fusion with unordered_list
        start_time = time()
        sorted_list = Fusion.fusion_sort(unordered_list)  # Call fusion_sort() on the Fusion instance
        stop_time = time()
        elapsed_time = (stop_time - start_time) * 1000
        print("\n", sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")

    if sort == 5:
        Quick = Quick (unordered_list)
        start_time = time()
        sorted_list = Quick.quick_sort(unordered_list)
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")

    if sort == 6:
        Heap = Heap (unordered_list)
        start_time = time()
        sorted_list = Heap.heap_sort(unordered_list)
        stop_time = time()
        elapsed_time = (stop_time - start_time)*1000
        print("\n",sorted_list)

        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms\n")



