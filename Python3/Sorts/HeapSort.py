"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module for heap sort

Requirements:
- None

Methods:
- heap_sort
- sift_down
"""

def heap_sort(a):
    l = len(a)

    if l < 2:
        return a

    # from last parent to first, sift down to make largest value at the top
    for j in range(l // 2, -1, -1):
        sift_down(a, j, l)

    # swap largest and smallest value and sift down
    for k in range(l - 1, -1, -1):
        a[0], a[k] = a[k], a[0]
        sift_down(a, 0, k)

    # send list, half of length, and length to heapify
    return a


def sift_down(a, i, l):
    c = i
    n = 2 * c + 1

    while n < l:
        if n < l - 1 and a[n] < a[n + 1]:
            n += 1

        if a[c] < a[n]:
            a[c], a[n] = a[n], a[c]
            c = n
            n = c * 2 + 1
        else:
            break
