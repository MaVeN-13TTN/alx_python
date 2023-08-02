def square_matrix_simple(matrix):
    return list(map(lambda row: list(map(lambda num: num**2, row)), matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
