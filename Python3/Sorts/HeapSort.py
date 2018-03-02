"""
Brian Taylor Vann
github.com/taylor-vann
"""

def heap_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    for j in range(length // 2, -1, -1):
        sift_down(arr, j, length)

    for k in range(length - 1, -1, -1):
        arr[0], arr[k] = arr[k], arr[0]
        sift_down(arr, 0, k)

    return arr


def sift_down(arr, start, finish):
    curr = start
    nxt = 2 * curr + 1

    while nxt < finish:
        if nxt < finish - 1 and arr[nxt] < arr[nxt + 1]:
            nxt += 1

        if arr[curr] < arr[nxt]:
            arr[curr], arr[nxt] = arr[nxt], arr[curr]
            curr = nxt
            nxt = curr * 2 + 1
        else:
            break
