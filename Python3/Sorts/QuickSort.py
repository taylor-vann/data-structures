"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to quick sort a list
- untraditional, copies list, more thread safe

Requirements:
- None

Methods:
- quick_sort
- partition
"""


def quick_sort(arr, start = 0, length = None):
    if length is None:
        length = len(arr)

    if length < 2:
        return arr

    pivot_index = partition(arr, start, length)

    left_length = pivot_index - start
    right_length = length - left_length - 1

    quick_sort(arr, start, left_length)
    quick_sort(arr, pivot_index + 1, right_length)

    return arr


def partition(arr, start, length):
    print("partition: ", arr)
    pivot = arr[start]
    barrier = start
    curr = start + 1
    last = start + length

    while curr < last:
        if arr[curr] < pivot:
            barrier += 1
            arr[barrier], arr[curr] = arr[curr], arr[barrier]
        curr += 1

    arr[start], arr[barrier] = arr[barrier], arr[start]
    return barrier
