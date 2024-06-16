# Author: Muyiwa Obadara
# Date: 27th December, 2023.
# Question: 4
"""A Python Module for Collatz Conjecture.
Data Structure and Algorithms 2

School of Physics, Engineering and Computer Science.
"""

def collatz(n: int) -> list:
    """This function returns the Collatz series of a given integer n.
    Args: n (int) input
    """
    collatz_series: list = []

    def collatz_constructor(n:int) -> list:
        nonlocal collatz_series
        # The input and output are integers
        # so, I use integer division, when dividing by 2.

        # Make sure that the argument is an integer and it is greater than zero.
        if n < 1 or not isinstance(n, int):
            raise ValueError("collatz(n): n must be an integer greater 0.")
        if n == 1:
            collatz_series.append(n)
        else:
            if n % 2 == 0:
                collatz_series.append(n)
                collatz_constructor(n//2)   
            else:
                collatz_series.append(n)
                collatz_constructor(3*n + 1)
        return collatz_series
    return collatz_constructor(n)