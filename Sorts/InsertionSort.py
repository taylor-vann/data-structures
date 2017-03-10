"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to insertion sort a list

Requirements:
- None

Methods:
- insetion_sort
"""

def insertion_sort(aList):
    if len(aList) == 0 or len(aList) == 1:
        return aList

    for i in range(len(aList) - 1):
        min_index = i

        for j in range(i + 1, 0, -1):
            if aList[j - 1] > aList[j]:
                aList[j - 1], aList[j] = aList[j], aList[j - 1]
