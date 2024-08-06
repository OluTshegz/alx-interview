#!/usr/bin/python3
"""
This module provides a function to calculate the
minimum number of operations needed to achieve exactly
`n` 'H' characters in a text file using only "Copy All"
and "Paste" operations.
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed
    to result in exactly n 'H' characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.
        Returns 0 if `n` is impossible to achieve.
    """
    # If n is less than or equal to 1, no operations can be performed
    if n <= 1:
        return 0

    # Initialize the number of operations to 0
    operations = 0

    # Start with the smallest factor (2)
    factor = 2

    # Continue while n is greater than 1
    while n > 1:
        # Check if the current factor divides n evenly
        while n % factor == 0:
            # If it does, add the factor to the operations count
            operations += factor
            # Reduce n by dividing it by the factor
            n //= factor

        # Increment the factor to check the next possible divisor
        factor += 1

    # Return the total number of operations
    return operations

# Note: Ensure that this file ends with a new line
