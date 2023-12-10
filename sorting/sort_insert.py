nums = [14,2,1,45,14,0,21,3,5,9,4,5,2,78,64]


for i in range(1,len(nums)):
    temp = nums[i]
    j = i-1
    
    while j>=0 and temp<nums[j]:
        nums [j+1] = nums[j]
        j = j-1
    nums[j+1] = temp
print(nums)