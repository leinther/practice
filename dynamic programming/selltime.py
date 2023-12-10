def maxProfit(prices):
    dp = [0]*len(prices)
    index = -1
    for i in range (len(prices)):
        for j in range(0,i+1):
            if j<=index:
                continue
            dp[i] = max(dp[i],prices[i]-prices[j])
            if prices[i]-prices[j]>0:
                index= i
    return dp
print(maxProfit(prices = [1,2,3,4,5]))



#Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#Total profit is 4 + 3 = 7.