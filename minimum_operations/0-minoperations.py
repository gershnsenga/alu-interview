#!/usr/bin/python3
""" The program Calculates the minimum number of operations to get n 'H' characters. """

def min_operations(n):
    """
    Calculate the minimum number of operations to get n 'H' characters.

    Args:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations, or 0 if impossible.
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


# Example usage and test
if __name__ == "__main__":
    test_cases = [3, 9, 12, 15]
    for case in test_cases:
        result = min_operations(case)
        print(f"n = {case}: {result} operations")

    # Specific example for n = 9
    print("\nDetailed example for n = 9:")
    print("H => Copy All => Paste => HH => Paste => HHH => "
          "Copy All => Paste => HHHHHH => Paste => HHHHHHHHH")
    print(f"Number of operations: {min_operations(9)}")