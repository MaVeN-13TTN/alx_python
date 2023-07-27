def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []
    for row in matrix:
        squared_row = []
        for num in row:
            squared_row.append(num ** 2)
        result_matrix.append(squared_row)
    return result_matrix
