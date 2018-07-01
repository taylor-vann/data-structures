"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def bubble_sort(arr):
    if len(arr) < 2:
        return arr

    swapped = True

    while swapped:
        swapped = False

        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

    return arr
