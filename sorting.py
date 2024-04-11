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

import math  

class Comb:
    def __init__(self, array):
        self.array = array

    def comb_sort(self, array):
        permutation = True
        gap = len(array)
        while (permutation == True) or  (gap>1):
            permutation = False
            gap = math.floor(gap / 1.3)
            if gap<1: gap = 1
            for current in range(0, len(array) - gap):
                if array[current] > array[current + gap]:
                    permutation = True
                    # On echange les deux elements
                    array[current], array[current + gap] = \
                    array[current + gap],array[current]

        return self.array
    
class Fusion:
    def __init__(self, arr):
        self.arr = arr

    # Divides the original list into 2 lists 
    def fusion(self, list_1, list_2):
        # Initiate the result list
        result = []
        # Starts with first element of the 2 lists
        index_list_1, index_list_2 = 0, 0
        # Goes through all the lists
        while index_list_1 < len(list_1) and index_list_2 < len(list_2):
            # For each index, takes the smallest element between the 2 lists
            if list_1[index_list_1] <= list_2[index_list_2]:
                # Adds it to the result list
                result.append(list_1[index_list_1])
                #  Goes to next index
                index_list_1 += 1
            else:
                result.append(list_2[index_list_2])
                index_list_2 += 1

        # If list_1 is not empty.
        if list_1:
            # Adds any remaining elements of list_1 to the result list.
            result.extend(list_1[index_list_1:])
        if list_2:
            result.extend(list_2[index_list_2:])
        return result
 

    def fusion_sort(self, m):
        # Base case: If the length of the list is 0 or 1, it's already sorted
        if len(m) <= 1:
            return m
        
        # Calculate the middle index of the list
        middle = len(m) // 2

        # Divide the original list into two sublists
        # First half of the list
        list_1 = m[:middle]
        # Second half of the list
        list_2 = m[middle:]

        # Recursively call fusion_sort on the two sublists to sort them
        list_1 = self.fusion_sort(list_1)
        list_2 = self.fusion_sort(list_2)

        # Merge the sorted sublists using the fusion method and return the result
        return list(self.fusion(list_1, list_2))
    
class Heap:
    def __init__(self, arr):
        self.arr = arr

    def heapify(self, arr, n, i):
        # Initialize largest as root
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # See if left child of root exists and is greater than root
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        # See if right child of root exists and is greater than the largest so far
        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            # Heapify the root.
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

        # Return the sorted array
        return self.arr

class Insertion():
    def __init__(self, arr):
        self.arr = arr

    def insertion_sort(self):
        # Runs through every element in the list
        for i in range(1,len(self.arr)):
            current = self.arr[i]
            j = i
            # Shifting of elements in the self.arr
            while j>0 and self.arr[j-1]>current:
                self.arr[j]=self.arr[j-1]
                j = j-1
            # We insert the element in its place
            self.arr[j]=current

        # Return the sorted array
        return self.arr
    
class Quick:
    def __init__(self, array):
        self.array = array 

    def quick_sort(self, array):

        if not array:
            return []
        else:
            pivot = array[-1]
            smallest = [x for x in array     if x <  pivot]
            biggest = [x for x in array[:-1] if x >= pivot]
            return self.quick_sort(smallest) + [pivot] + self.quick_sort(biggest)

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

