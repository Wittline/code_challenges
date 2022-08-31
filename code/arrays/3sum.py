def two(nums, i, resp):
    lo, hi = i +1, len(nums) -1
    while lo < hi:
        ss = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif ss > 0:
            hi -= 1
        else:
            resp.append(nums[i],nums[lo],nums[hi])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo -1]:
                lo +=1

def Threesum(nums):
    resp = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break

        if i == 0 or nums[i-1] != nums[i]:
            two(nums, i, resp)
    
    return resp