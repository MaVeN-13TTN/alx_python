def square_values(matrix):
    square_matrix = list(map(lambda row: list(map(lambda num: num**2, row)), matrix))
    return square_matrix
matrix=[[]]
result_matrix = square_values()
print(result_matrix)
print(matrix)
