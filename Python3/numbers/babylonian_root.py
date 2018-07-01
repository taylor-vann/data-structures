"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def babylonian_root(n, precision = 0.00001):
    if n < 0:
        return None

    if n == 0:
        return 0

    g1 = n / 2
    g2 = g1 + 1

    while(abs(g2 - g1) > precision):
        num = n / g1
        g2 = g1
        g1 = (g1 + num) * 0.5

    return g1
