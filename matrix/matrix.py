def rotate(matrix):
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))