"""
Brian Taylor Vann
github.com/taylor-vann
"""


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    point = len(arr) // 2

    left = merge_sort(arr[:point])
    right = merge_sort(arr[point:])

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result += [left.pop(0)]
        else:
            result += [right.pop(0)]

    result += left
    result += right

    return result
