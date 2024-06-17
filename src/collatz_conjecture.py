"""Collatz Conjecture
"""
def collatz(n: int) -> list:
    """Returns the Collatz series for the given integer.
    
    Args: n (int) input integer
    
    Returns: collatz_series (list) the Collatz series for the given integer.
    """
    collatz_series: list = []

    def collatz_constructor(n:int) -> list:
        nonlocal collatz_series
        # The input and output are integers
        # I used integer division, when dividing by 2.

        # Make sure the argument is an integer and it is greater than zero.
        if not (n > 0 and isinstance(n, int)):
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