"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

def newtonian_root(n, precision = 0.0000001):
    if n < 0:
        return None

    if n == 0:
        return 0

    delta_prime = n
    delta_curr = n / delta_prime

    while(abs(delta_prime - delta_curr) > precision):
        delta_prime = (delta_curr + delta_prime) * 0.5
        delta_curr = n / delta_prime

    return delta_prime
