"""
Brian Taylor Vann
github.com/taylor-vann
"""

def bubble_sort(arr):
    if len(arr) < 2:
        return arr

    swapped = True

    # until list is traversed without swapping ...
    while swapped:
        swapped = False
        # if prev is less than next then swap ...
        for j in range(len(arr) - 2):
            # if prev is less than next then swap ...
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
    
    return arr
