def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    else:
        for row in matrix:
            for i, num in enumerate(row):
                if i == len(row) - 1:
                    print("{:4d}".format(num))
                else:
                    print("{:4d}".format(num), end=" ")
        
        
