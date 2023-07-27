def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.
    Args:
        matrix: A list of lists of integers.
    Returns:
        None.
    """
    # Check if the matrix is empty.
    if not matrix:
        return
    # Print the first row of the matrix.
    print(" ".join(str(i) for i in matrix[0]))
    # Print the remaining rows of the matrix.
    for row in matrix[1:]:
        print(" ".join(str(i) for i in row))