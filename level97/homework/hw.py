import math

def is_square(n):
    if n < 0:
        return False
    root = math.isqrt(n)  # integer square root (Python 3.8+)
    return root * root == n
