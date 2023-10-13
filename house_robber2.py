def rob(nums):
    dp = [0] * len(nums)
    for i in range (len(nums)):
        dp[i] = max(dp[i-2],nums[i]+dp[i-2])
    return dp

print(rob(nums = [200,3,140,20,10])) 