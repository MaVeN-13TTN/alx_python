def square_values(matrix):
    # Use map() and lambda to compute the square of all integers in the matrix
    square_matrix = list(map(lambda row: list(map(lambda num: num**2, row)), matrix))
    return square_matrix

result_matrix = square_values([[1, 2], [4, 5], [7, 8]])
print(result_matrix)
