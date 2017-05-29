"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Get the greatest common denominator

Requirements:
- None

Methods:
- gcd(number 1, number 2)
"""

def gcd(n, m):
    while m:
    	n, m = m, n % m

    return n
