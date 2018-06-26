"""
Brian Taylor Vann
github.com/taylor-vann
"""

def insertion_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    for j in range(1, length):
        for k in range(j, 0, -1):
            if not arr[k - 1] > arr[k]:
                break
            
            arr[k - 1], arr[k] = arr[k], arr[k - 1]

    return arr
