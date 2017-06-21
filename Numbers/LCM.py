"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Get the least common multiple

Requirements:
- None

Methods:
- lcm(number 1, number 2)
"""

from GCD import gcd


def lcm(n, m):
    if type(n) != int and type(m) != int:
        return

    r = n / gcd(n, m)
    r *= m

    return r
