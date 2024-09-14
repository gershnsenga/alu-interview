#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of operations
required to obtain n 'H' characters in a file, given only 'Copy All' and 'Paste'
operations.

The main function, min_operations, takes an integer n as input and returns
the minimum number of operations needed to achieve n 'H' characters, starting
with a single 'H'.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations to get n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations, or 0 if impossible.

    Examples:
        >>> min_operations(9)
        6
        >>> min_operations(1)
        0
        >>> min_operations(0)
        0
        >>> min_operations(-12)
        0
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations


if __name__ == "__main__":
    test_cases = [21, 19170307, 972, 1, 0, -12, 2147483640]
    for case in test_cases:
        result = minOperations(case)
        print(f"n = {case}: {result} operations")