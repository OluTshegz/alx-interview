#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island described in a grid.

    Args:
        grid (list of list of int): A list of lists where
        0 represents water and 1 represents land. The grid is
        surrounded by water and contains only one island.

    Returns:
        int: The perimeter of the island.
    """
    # Check for an empty grid (no rows or columns)
    if not grid or not grid[0]:
        return 0  # Return 0 for an empty grid

    # Initialize perimeter variable to store
    # the total perimeter of the island
    perimeter = 0

    # Loop through every cell in the grid
    for i in range(len(grid)):  # i represents the row index
        for j in range(len(grid[i])):  # j represents the column index
            if grid[i][j] == 1:  # Check if the current cell is land
                # Add 4 for each land cell (each cell starts with 4 sides)
                perimeter += 4

                # Check for neighboring land cells,
                # subtract 2 for each shared side
                if i > 0 and grid[i - 1][j] == 1:  # Check cell above
                    # Subtract 2 for shared border
                    # with the land cell above
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:  # Check cell to the left
                    # Subtract 2 for shared border with
                    # the land cell to the left
                    perimeter -= 2

    return perimeter  # Return the total calculated perimeter
