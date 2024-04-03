import random
from TriBulle import TriBulle

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

    length = int(input ("Choisissez une longueur de liste : "))
    min_value = 0.1
    max_value = 1000.0

    createList = CreateList(length, min_value, max_value)
    unordered_list = createList.generate_list()
    print(f"La liste de {length} nombres réels à été générée.")

    tribulle = TriBulle (unordered_list)
    sorted_list = tribulle.bubblesort()
    print("Liste triée :", sorted_list)


