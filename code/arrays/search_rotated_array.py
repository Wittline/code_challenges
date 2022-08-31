def serach_in_rotated(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        middle = l + (r - l) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] >= nums[l]:
            if target >= nums[l] and target < nums[middle]:
                r = middle - 1
            else:
                l = middle + 1
        else:
            if target <= nums[r] and target > nums[middle]:
                l = middle + 1
            else:
                r = middle -1
    return -1

