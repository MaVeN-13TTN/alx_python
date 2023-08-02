def square_matrix_simple(matrix=[]):
    square_matrix = list(map(lambda row: list(map(lambda num: num**2, row)), matrix))
    return square_matrix

matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = square_matrix_simple()
print(new_matrix)
print(matrix)
