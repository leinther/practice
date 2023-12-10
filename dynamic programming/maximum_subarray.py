def maxSubArray(nums):
    answer = []
    summ = 0
    
    def dfs (array,summ,ans):
        if len(array)>1:
            L = dfs (array [:len(array)//2],summ,ans)
            R = dfs (array [len(array)//2:],summ,ans)
            if sum (array)>sum(ans):
                ans = array
        answer = ans    
    return dfs (nums.copy(),0,[])    
       
        
print (maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))