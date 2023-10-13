def comb (nums):
    ans = []
    used = [False]*len(nums) [False,False,False]
    
    def dfs(ans,curr,nums,used):
        if len(curr) == len(nums):
            ans.append(curr[::])
            return
            
        for i in range(len(nums)):
            if not used[i]:
                curr.append(nums[i])
                used[i] = True
                dfs(ans,curr,nums,used)
                
                curr.pop()
                used[i]=False
    dfs(ans,[],nums,used,0)
    return ans
    
    
print(comb([1,2,3,4]))