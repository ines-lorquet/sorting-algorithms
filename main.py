import random, statistics, os
from sorting import *
from time import time
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

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

def plot_unordered_list(unordered_list):
    plt.figure(figsize=(10, 5))
    plt.plot(unordered_list, color='gray', label='Non triée')
    plt.xlabel('Indice des éléments')
    plt.ylabel('Valeurs aléatoires')
    plt.title('Liste non triée')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    # Asks the user the size of the list, creates the list
    length = int(input ("\nChoisissez une longueur de liste : "))
    min_value = 0.1
    max_value = 1000.0
    createList = CreateList(length, min_value, max_value)
    unordered_list = createList.generate_list()
    print(f"\nLa liste de {length} nombres réels à été générée.\n")

    # Prints the available sorting methods
    for i in range(1,8):
        print(f"Tri {['sélection', 'bulle', 'insertion', 'fusion', 'rapide', 'par tas', 'à peigne'][i-1]} - \033[94m{i}\033[0m")

    # Asks the user which method he wishes to execute
    sort = int(input("\nChoisissez le chiffre correspondant à la méthode de tri voulue : "))

    # Mapping the sort methods and their corresponding classes
    sorting_methods = {
        1: (Selection, "tri par sélection"),
        2: (Bulle, "tri à bulle"),
        3: (Insertion, "tri par insertion"),
        4: (Fusion, "tri par fusion"),
        5: (Quick, "tri rapide"),
        6: (Heap, "tri par tas"),
        7: (Comb, "tri par peigne")
    }

    # Executes the sorting method & displays the graphic
    if sort in sorting_methods:
        sorting_class, method_name = sorting_methods[sort]
        sorting_instance = sorting_class(unordered_list)
        
        start_time = time()

        if hasattr(sorting_instance, 'sort_method'):
            sorted_list = sorting_instance.sort_method()
        else:
            sorted_list = sorting_instance.selection_sort() if sort == 1 else sorting_instance.bubble_sort() if sort == 2 else sorting_instance.insertion_sort() if sort == 3 else sorting_instance.fusion_sort(unordered_list) if sort == 4 else sorting_instance.quick_sort(unordered_list) if sort == 5 else sorting_instance.heap_sort(unordered_list) if sort == 6 else sorting_instance.comb_sort(unordered_list) if sort == 7 else None

        stop_time = time()
        elapsed_time = (stop_time - start_time) * 1000
        
        print("\n", sorted_list)
        print(f"\nListe de \033[94m{length}\033[0m entrées triée en \033[94m{elapsed_time:.2f}\033[0m ms avec la méthode du \033[94m{method_name}\033[0m.\n")

        # Creates the graph
        plt.figure(figsize=(10, 5))
        # Définit l'intervalle des abscisses
        plt.xlim(0, len(sorted_list) - 1)
        # Définit l'intervalle des ordonnées
        plt.ylim(min(sorted_list), max(sorted_list))

        for i in range(len(sorted_list)):
            # Updates the graph at each iteration
            plt.plot(sorted_list[:i+1], color='blue', label='Tri en cours')
            plt.xlabel('Nombre d\'éléments')
            plt.ylabel('Valeurs')
            plt.title(f'Progression du tri - {method_name}')
            plt.tight_layout()
            plt.pause(0.05)
        # maintains the graph after the scripts ends  
        plt.show(block=True)



        # Creates the Markdown table
        table = f"| {length} | {method_name} | {elapsed_time:.3f} ms |\n"

        # Creates the README.md file if needed
        if not os.path.exists("README.md"):
            with open("README.md", "w") as readme_file:
                readme_file.write("| Nombre d'entiers naturels dans la liste | Méthode de tri | Temps d'exécution  |\n")
                readme_file.write("| -------------- | ------------- | ----------------- |\n")
                readme_file.write(table)
        #  Writes a new line in the table in README.md
        else:
            try:
                with open("README.md", "a") as readme_file:
                    readme_file.write(table)
                print("Une ligne a été ajoutée avec succès au fichier README.md.")
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'ajout de la ligne au fichier README.md : {e}")

    else:
        print("La méthode de tri sélectionnée n'est pas valide.")


