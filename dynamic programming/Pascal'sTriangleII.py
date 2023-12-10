def getRow(rowIndex):
    matrix = [[0]*i for i in range(1,rowIndex+2)]

    for x in range (0,rowIndex+1):
        matrix[x][(len(matrix[x])-1)],matrix[x][0] = 1,1
        for y in range (1,x):
            if x <2:break 
            else:matrix [x][y] = matrix [x-1][y] + matrix [x-1][y-1]
    return matrix[rowIndex]
    
    
print(getRow(rowIndex = 0))