"""
Brian Taylor Vann
github.com/taylor-vann
"""

def insertion_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    for j in range(1, length):
        curr = j
        prv = j - 1

        while prv > -1 and arr[prv] > arr[curr]:
            arr[prv], arr[curr] = arr[curr], arr[prv]
            curr -= 1
            prv = curr - 1

    return arr
