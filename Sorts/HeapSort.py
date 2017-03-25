"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module for heap sort

Requirements:
- None
"""

def HeapSort(a):
    l = len(a) - 1

    if l < 1:
        return

    heapify(a)

    for i in range(l, -1, -1):
        a[0], a[i] = a[i], a[0]
        perc_down(a, 0, i)


def heapify(a):
    l = len(a)

    b = l // 2

    while b > -1:
        perc_down(a, b, l)
        b -= 1


def perc_down(a, i, l):
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
