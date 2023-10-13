def rob(nums):
    n = 0 
    t = 0 
    for i in nums:
        temp = max (t, n+i)
        n = t 
        t = temp 
    return t

print (rob(nums = [2,3,2]))