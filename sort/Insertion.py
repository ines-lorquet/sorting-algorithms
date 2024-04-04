class Insertion():
    def __init__(self, arr):
        self.arr = arr

    def insertion_sort(self):
        # runs through every element in the list
        for i in range(1,len(self.arr)):
            current = self.arr[i]
            j = i
            #décalage des éléments du self.arr }
            while j>0 and self.arr[j-1]>current:
                self.arr[j]=self.arr[j-1]
                j = j-1
            #on insère l'élément à sa place
            self.arr[j]=current

        # Return the sorted array
        return self.arr