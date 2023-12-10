def uniquePaths(m,n):
    dp = [[1]*n for i in range (m)]
    for x in range (1,m):
        for y in range (1,n):
            dp[x][y] = dp[x-1][y]+dp[x][y-1]
    return dp[-1][-1]
print(uniquePaths(m = 3, n = 7))

[[1, 1, 1, 1, 1,   1,  1], 
 [1, 2, 3, 4,  5,  6,  7], 
 [1, 3, 6, 10, 15, 21, 28]]

[[1, 2, 3, 4, 5, 6, 7], 
 [2, 4, 7, 11, 16, 22, 29], 
 [3, 7, 14, 25, 41, 63, 92]]

[[1, 2], 
 [2, 4], 
 [3, 7]]

[[1, 2], 
 [1, 1], 
 [1, 1]]