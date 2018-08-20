"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def gcd(n, m):
    if m == 0:
        return n

    return gcd(m, n % m)
