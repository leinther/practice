def rob(nums):
    d1 = nums[0]
    d2 = max(nums [1],nums[0])
    for i in range (2,len(nums)):
        temp = d1+nums[i]
        d1 = max(d2,d1)
        d2 = temp
    return max(d2,d1)
print (rob(nums = [1,2]))