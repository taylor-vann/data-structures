"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Get root with Newton method

Requirements:
- None

Methods:
- sqrt_newton()
"""

def sqrt_newton(n):
    if n < 0:
        return None

    if n == 0:
        return 0

    g1 = n * 0.5
    g2 = n

    while(True):
        g2 = (g1 + (n / g1)) * 0.5

        if g1 == g2:
            break

        g1 = g2

    return g2
