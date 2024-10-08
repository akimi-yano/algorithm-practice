# 1437. Check If All 1's Are at Least Length K Places Away
# Easy

# 208

# 166

# Add to List

# Share
# Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

 

# Example 1:



# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# Example 2:



# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
# Example 3:

# Input: nums = [1,1,1,1,1], k = 0
# Output: true
# Example 4:

# Input: nums = [0,1,0,1], k = 1
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= k <= nums.length
# nums[i] is 0 or 1

# This solution works:

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if sum(nums) == 0:
            return True
        start = nums.index(1)
        d = None
        for i in range(start, len(nums)):
            if nums[i] == 1:
                if d is not None and d < k:
                    return False
                d = 0
            else:
                d += 1
        return True