def sor (nums):
    for i in range (len(nums)):
        idx = i
        for e in range(i+1,len(nums)):
            if nums[e]<nums[idx]:
                idx = e
        nums[i],nums[idx] = nums[idx],nums[i]
        
    
    return nums

print(sor([1312,23,124,111,2,314,0,0,213]))