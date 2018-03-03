"""
Brian Taylor Vann
github.com/taylor-vann
"""


def selection_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    for i in range(length):
        index = i

        for j in range(i + 1, length):
            if arr[j] < arr[index]:
                index = j

        if index != i:
            arr[index], arr[i] = arr[i], arr[index]

    return arr
