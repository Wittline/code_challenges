
# HARD
#nums = [1, 3, 4,2,2]
# output: 2

def find_duplicate(nums):

    slow , fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

        
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow

