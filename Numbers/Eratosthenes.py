"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Run the Sieve of Eratosthenes

Requirements:
- None

Methods:
- sieve(n)
"""

def sieve(n):
    l = n + 1
    rng = list(range(l))
    rslt = []

    ind = 2
    i = ind + ind


    while ind < l:
        while i < l:
            rng[i] = None
            i += ind

        ind += 1
        while ind < l and rng[ind] == None:
            ind += 1

        i = ind + ind

    for j in range(1, l):
        if rng[j] != None:
            rslt.append(rng[j])

    return rslt
