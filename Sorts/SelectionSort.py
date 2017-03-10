"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to selection sort a list

Requirements:
- None

Methods:
- selection_sort
"""


def selection_sort(aList):
    if len(aList) == 0 or len(aList) == 1:
        return aList

    for i in range(len(aList)):
        min_index = i

        for j in range(i + 1, len(aList)):
            if aList[j] < aList[min_index]:
                min_index = j

        if min_index != i:
            aList[min_index], aList[i] = aList[i], aList[min_index]
