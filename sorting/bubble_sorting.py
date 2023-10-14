def bubble(nums):
    for i in range(len(nums)):
        flag=False
        for e in range(0,len(nums)-i-1):
            if nums[e+1]<nums[e]:
                nums[e],nums[e+1] = nums[e+1],nums[e]
                flag = True
        if flag is False:
            return nums
    
    
print(bubble([1,4,2,5,3,0,0,0,0]))