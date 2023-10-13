def subsets(nums):
    ans = [[]]
    def dfs (sub,depth):
        if depth == len(nums) or len(sub)>=len(nums):
            return
        sub.append(nums[depth])
        ans.append(sub.copy())
        dfs (sub,depth+1)
        sub.pop()
        dfs (sub,depth+1)
    dfs([],0)
    return ans 
    
    
print(subsets(nums = [1,2,2]))