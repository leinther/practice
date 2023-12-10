def rob(nums):
    dp = nums[0],max(nums[0],nums[1])
    
    for i in range(2,len(nums)):
        dp = dp[1],max(dp[0]+nums[i-2],dp[1])
    return dp   

print(rob(nums = [200,3,140,20,10])) 