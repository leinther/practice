def minPathSum(grid):
    for i in range (len(grid)):
        for e in range (len(grid[i])):
            if i==0 and e>=1:
                grid [i][e] += grid[i][e-1]
            elif i>=1 and e==0:
                grid [i][e]+= grid [i-1][e]
            elif i>=1 and e>=1:
                grid[i][e] = min(grid[i][e-1]+grid[i][e],grid[i-1][e]+grid[i][e])    
    return grid[-1][-1]

print(minPathSum(grid = [[1,3]]))

[1,3,1],
[1,5,1],
[4,2,1]

[[1, 4, 5], 
 [2, 7, 6], 
 [6, 8, 7]]