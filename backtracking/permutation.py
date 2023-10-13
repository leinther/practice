def permute(nums):
    res = []
    used = [False]*len(nums)
    def dfs (sub):
        if len(sub)==len(nums):
            res.append(sub.copy())
        else:
            for i in range(len(nums)):
                if used[i] is True:
                    continue
                sub.append(nums[i])
                used[i] = True 
                dfs (sub)
                used[i]=False
                sub.pop()         
    dfs([])
    return res
print (permute([1,2,3]))
        