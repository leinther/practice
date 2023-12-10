def rob(nums):
    if len(nums) < 3: return max(nums)
    def lr (nums):
        M = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            M = M[1], max(nums[i]+M[0], M[1])
        return M[1]
    return max(lr (nums[1::]), lr (nums[:-1]))
print (rob(nums = [4,1,2,7,5,3,1]))