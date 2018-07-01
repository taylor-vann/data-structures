"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def greatest_common_denominator(n, m):
    if m == 0:
        return n

    return greatest_common_denominator(m, n % m)
