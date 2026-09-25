#!/usr/bin/python3
"""
Module containing the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for row_idx in range(1, n):
        previous_row = triangle[-1]
        current_row = [1]
        for col_idx in range(1, row_idx):
            current_row.append(previous_row[col_idx - 1] + previous_row[col_idx])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
