#!/usr/bin/python3
"""
Module for UTF-8 Validation.
"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the data set to validate.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    number_of_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7

        if number_of_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & byte:
                number_of_bytes += 1
                mask = mask >> 1

            # If number_of_bytes is 0, then it is a 1-byte character
            if number_of_bytes == 0:
                continue

            # UTF-8 characters can be between 1 and 4 bytes long
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False

        else:
            # The next bytes should start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes to check for the next byte
        number_of_bytes -= 1

    # If we have checked all the bytes and number_of_bytes is 0, return True
    return number_of_bytes == 0
