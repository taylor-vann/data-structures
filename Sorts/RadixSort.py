"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Module to Radix sort a list

Requirements:
- Assumes whole numbers (pos ints: 0, 1, 2, ...)

Methods:
- radix_sort
- bucketish_sort
- get_max
"""


def radix_sort(aList, base = 10):
    if len(aList) <= 1:
        return aList

    bucket = aList
    exp = base
    mod = 1
    max_num = get_max(aList)

    while max_num//mod > 0:
        bucket = bucketish_sort(bucket, exp, mod)
        exp *= base
        mod *= base

    return bucket


def bucketish_sort(aList, exp, mod, base = 10):
    bucket = []

    for i in range(base):
        bucket.append([])

    coll = []

    for val in aList:
        index = (val % exp)//mod
        bucket[index].append(val)

    for var in bucket:
        coll += var

    return coll


def get_max(aList):
    if len(aList) == 0:
        return None

    num = aList[0]

    for var in aList:
        if num < var:
            num = var

    return num
