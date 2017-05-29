"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Get root with a more familiar Newton Method

Requirements:
- None

Methods:
- sqrt_rnewton()
"""

def sqrt_rnewton(n):
    if n < 0:
        return None

    if n == 0:
        return 0

    g1 = n * 0.5
    g2 = n

    i = 0

    while(i < 20):
        g2 = g1 - ((g1 * g1 - n) / (2 * g1))

        if g1 == g2:
            break

        g1 = g2
        i += 1

    return g2
