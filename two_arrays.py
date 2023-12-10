def intersection(nums1, nums2):
    small = nums1 if len(nums1)<len(nums2) else nums2
    large = nums1 if len(nums1)>len(nums2) else nums2
    ans = []
    x,y = 0,0
    
    while x <=(len(small)-1):
        if y > (len(large))-1:
            x+=1
            y=0
            continue
        if small[x] == large[y]:
            if small[x] not in ans:
                ans.append(small[x])
        y+=1
    return ans
print(intersection(nums1 = [4], nums2 = [4]))# nums1 = [1,2,2,1], nums2 = [2,2]