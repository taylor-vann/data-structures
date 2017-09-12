"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Get the root with Babylonian method 

Requirements:
- None

Methods:
- sqrt_babylon()
"""

def sqrt_babylon(n):
    if n < 0:
        return None

    if n == 0:
        return 0

    g1 = n / 2
    g2 = g1 + 1

    while(g1 != g2):
        num = n / g1
        g2 = g1
        g1 = (g1 + num) * 0.5

    return g1
