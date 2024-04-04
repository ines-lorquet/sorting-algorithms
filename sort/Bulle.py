class Bulle:
    def __init__(self, arr):
        self.arr = arr

    def bubble_sort(self):
        # Get the length of the array
        n = len(self.arr)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place, no need to compare them
            for j in range(0, n-i-1):

                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if self.arr[j] > self.arr[j+1] :
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

        # Return the sorted array
        return self.arr



  