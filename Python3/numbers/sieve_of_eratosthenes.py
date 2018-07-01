"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def sieve_of_eratosthenes(n):
    if type(n) != int:
        return None

    tally = [i for i in range(1, n + 1)]

    for j in range(2, n + 1):
        for k in range(j * 2, n + 1, j):
            tally[k - 1] = None

    return [mark for mark in tally if mark != None]
