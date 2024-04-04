def tri_peigne(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap !=1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr
