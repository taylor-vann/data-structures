"""
Brian Taylor Vann
github.com/taylor-vann
"""


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    point = len(arr) // 2

    return merge(
        merge_sort(arr[:point]),
        merge_sort(arr[point:]))


def merge(left, right):
    result = []

    while left and right:
        if left[-1] > right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())

    return reversed(result) + left + right
