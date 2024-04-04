class Fusion:
    def __init__(self, arr):
        self.arr = arr

    # divides the original list into 2 lists 
    def fusion(self, list_1, list_2):
        # Initiate the result list
        result = []
        # Starts with first element of the 2 lists
        index_list_1, index_list_2 = 0, 0
        # Goes through all the lists
        while index_list_1 < len(list_1) and index_list_2 < len(list_2):
            # for each index, takes the smallest element between the 2 lists
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
            # adds any remaining elements of list_1 to the result list.
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
    