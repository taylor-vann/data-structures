"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

from greatest_common_denominator import gcd


def least_common_multiple(num1, num2):
    if type(num1) != int and type(num1) != int:
        return

    multiple = num1 / gcd(num1, num2)

    return multiple * num2
