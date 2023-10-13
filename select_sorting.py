<<<<<<< HEAD
def select_sorting(nums):
    for i in range (len(nums)):
        ind = i
        for e in range (i+1,len(nums)):
            if nums[e]<nums[ind]:
                ind = e 
        nums[i],nums[ind] = nums[ind],nums[i]
            
    return nums

print(select_sorting([56,3,2,4,6,5,4,68,12,32,4,1]))        
=======
def sor (nums):
    for i in range (len(nums)):
        idx = i
        for e in range(i+1,len(nums)):
            if nums[e]<nums[idx]:
                idx = e
        nums[i],nums[idx] = nums[idx],nums[i]
        
    
    return nums

print(sor([1312,23,124,111,2,314,0,0,213]))
>>>>>>> 1b9ee5bdd13ca787596b239ef076534474b53bdb
