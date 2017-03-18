"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to bubble sort a list

Requirements:
- None

Methods:
- bubble_sort
"""

def bubble_sort(aList):
    if len(aList) <= 1:
        return

    for i in range(len(aList)):
        for j in range(i + 1, len(aList)):
            if aList[i] > aList[j]:
                aList[i], aList[j] = aList[j], aList[i]
