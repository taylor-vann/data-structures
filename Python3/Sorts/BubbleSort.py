"""
Brian Taylor Vann
github.com/taylor-vann
"""

def bubble_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    swapped = False

    while not swapped:
        for i in range(length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False

    return arr
