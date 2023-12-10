def generateParenthesis(n):
    comb = []
    def dfs (sub,left,right):
        if len(sub)==n*2:
            comb.append(sub)
            return 
        if left<n:
            dfs(sub+"(",left+1,right)
        if right<left:
            dfs(sub+")",left,right+1)
            
            
    dfs ("", 0,0)
    return comb
    
print(generateParenthesis(3))