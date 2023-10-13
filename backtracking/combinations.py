def combine(n,k):
    nums = [i for i in range (1,n+1)]
    ans = []

    def dfs(sub,depth):
        if len(sub)==k :
            ans.append(sub.copy())
            return
        if depth>=len(nums):
            return
        sub.append(nums[depth])
        dfs(sub,depth+1)
        sub.pop()
        dfs(sub,depth+1)
                    
    dfs([],0)
    return ans
    
print(combine(n = 4, k = 3))