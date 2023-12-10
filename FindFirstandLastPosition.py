def searchRange(nums,target):
    low,high = 0, len(nums)-1
    while low < high:
        mid = (low + high)//2
        if nums [low] and nums[high]  == target:
            return low,high 
        if nums[mid] == target:
            low = mid
        elif nums [mid] > target:
            high = mid
    
    
print(searchRange(nums = [5,7,7,8,8,10], target = 8))