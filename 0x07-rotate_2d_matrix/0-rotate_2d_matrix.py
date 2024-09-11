#!/usr/bin/python3
"""
Module to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): 2D matrix to be rotated.

    Returns:
        None
    """
    n = len(matrix)  # Get the size of the matrix (n x n)

    # First, transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then, reverse each row to complete the 90-degree rotation
    for i in range(n):
        matrix[i].reverse()  # Reverse the current row


if __name__ == "__main__":
    # Test the rotation with a sample matrix
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)  # Rotate the matrix in place
    print(matrix)  # Output the rotated matrix
