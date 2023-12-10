def combine(n, k):
    ans = []
    
    def dfs (s,path):
        if len(path)==k:
            ans.append(path.copy())
            return 
        
        for i in range(s,n+1): # 1 - (1), 2 -(2) 
            path.append(i)
            dfs (s+1,path)
            path.pop()
 
    dfs(1,[])
    
    
    
    return ans



print (combine(n = 2, k = 2))