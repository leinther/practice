def searchInsert(nums, target):

    def search (low,high):
        if high>=low:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] <target:
                return search(mid+1,high)
            elif nums[mid]>target:
                return search (low, mid-1)
        else:
            return max(low,high)
            
    print(search(low = 0,high = len(nums)-1))
    
    
print (searchInsert(nums = [1,3,5,7], target = 0))
