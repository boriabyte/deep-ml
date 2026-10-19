import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    no_rows = len(a)
    no_cols = len(a[0])

    res = []
    col = []

    for i in range(no_cols):
        col = []
        for j in range(no_rows):
            col.append(a[j][i])
        res.append(col)
    
    return res




