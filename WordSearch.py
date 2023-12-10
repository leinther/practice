def exist(board, word):
    path = ""
    def dfs (x,y,i):
        if board[x][y] == word[i]:
            path+=word[i]
            dfs(x,y+1,i+1)
        else:
            dfs(x)    
    dfs (0,)
    
    return
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))