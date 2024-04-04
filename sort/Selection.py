class Selection:
    def __init__(self, arr):
        self.arr = arr
    
    def selection_sort(self):
        nb = len(self.arr)
        for current in range(nb):    
            smallest = current
            for j in range(current+1,nb) :
                if self.arr[j] < self.arr[smallest] :
                    smallest = j
            if smallest != current :
                temp = self.arr[current]
                self.arr[current] = self.arr[smallest]
                self.arr[smallest] = temp
        # Return the sorted array
        return self.arr
