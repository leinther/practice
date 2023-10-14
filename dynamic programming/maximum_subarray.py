def maxSubArray(nums):
    ans = []
    summ = None
    def divide(num,summ,cur):
        if len(num) > 1:
            mid = len(num)//2 
            L = divide(num[:mid],sum(num),cur)
            R = divide (num[mid:],sum(num),cur)
            if summ>sum(ans):
                cur = num
            
        return cur   
        
        
    divide(nums.copy(),None,[])
    return nums

print (maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))