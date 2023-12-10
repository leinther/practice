def minCostClimbingStairs(cost):
    dp = [0]*(len(cost)+1)
    dp[0],dp[1] = cost[0],cost[1]
    
    for i in range (2,len(cost)):
        dp[i] = min (dp[i-1]+cost[i],dp[i-2]+cost[i])
            
    return min(dp[(len(dp)-1)-1],dp[(len(dp)-1)-2])
print (minCostClimbingStairs(cost = [10,15,20]))