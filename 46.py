def permute(nums):
    ans = []
    used = [False] * len(nums)

    def dfs(path):
        if len(path) == len(nums):
            if path not in ans:
                ans.append(path.copy())
                return
        for i in range(len(nums)):             #помечаем пройденые вершины и когда все будут True начинаем скручивать стек где убираем по элементу из посещённой вершины
            if used [i] is not True:
               path.append(nums[i])
               used[i]=True
               dfs(path)
               used [i] = False
               path.pop()
nums.sort()
    dfs([])
    
    return ans
print (permute([1,1,2]))

