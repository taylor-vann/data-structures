"""
Brian Taylor Vann
github.com/taylor-vann
"""

def heap_sort(arr):
    if len(arr) < 2:
        return arr

    for j in range(len(arr) // 2, -1, -1):
        sift_down(arr, j, len(arr))

    for k in range(len(arr) - 1, -1, -1):
        arr[0], arr[k] = arr[k], arr[0]
        sift_down(arr, 0, k)

    return arr


def sift_down(arr, first, last):
    curr = first
    nxt = 2 * curr + 1

    while nxt < last:
        if nxt < last - 1 and arr[nxt] < arr[nxt + 1]:
            nxt += 1

        if arr[curr] > arr[nxt]:
            break

        arr[curr], arr[nxt] = arr[nxt], arr[curr]
        curr, nxt = nxt, curr * 2 + 1