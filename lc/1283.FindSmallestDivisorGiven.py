# 1283. Find the Smallest Divisor Given a Threshold
# Medium

# 514

# 85

# Add to List

# Share
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# It is guaranteed that there will be an answer.

 

# Example 1:

# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
# Example 2:

# Input: nums = [2,3,5,7,11], threshold = 11
# Output: 3
# Example 3:

# Input: nums = [19], threshold = 5
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^6
# nums.length <= threshold <= 10^6

# This solution works !
'''
use math.ceil to verify the sum
binary search
dont include 0 in binary search to avoid zero division - left = 1 to initialize
if the helper return True, any number smaller than that is eliminated, so move the right = mid
if its invalid, move left = mid+1
'''

import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            if self.helper(mid, nums, threshold):
                right = mid
            else:
                left = mid+1
        return left
    
    def helper(self, divisor, nums, threshold):
        total = 0
        for num in nums:
            total += math.ceil(num/divisor)
        if total <= threshold:
            return True
        else:
            return False