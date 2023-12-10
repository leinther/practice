def select_sorting(nums):
    for i in range (len(nums)):
        ind = i
        for e in range (i+1,len(nums)):
            if nums[e]<nums[ind]:
                ind = e 
        nums[i],nums[ind] = nums[ind],nums[i]
            
    return nums

print(select_sorting([56,3,2,4,6,5,4,68,12,32,4,1]))        
