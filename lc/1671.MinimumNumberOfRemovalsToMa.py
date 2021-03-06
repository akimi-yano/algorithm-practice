# 1671. Minimum Number of Removals to Make Mountain Array
# Hard

# 64

# 0

# Add to List

# Share
# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

 

# Example 1:

# Input: nums = [1,3,1]
# Output: 0
# Explanation: The array itself is a mountain array so we do not need to remove any elements.
# Example 2:

# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
# Example 3:

# Input: nums = [4,3,2,1,1,2,3,1]
# Output: 4
# Example 4:

# Input: nums = [1,2,3,4,4,3,2,1]
# Output: 1
 

# Constraints:

# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 109
# It is guaranteed that you can make a mountain array out of nums.

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Some change to update the dp array with all 0s (only +1 once there's increasing or deceasing)
        # and then add if condition (non zero since we need a peak) during sweeping the array...
        # Left to right: Find the maximum increasing subarray ends at pos[i]
        # Right to left： Find the maximum decreasing subarray ends at pos[i]
        # Sweep the array one more time to find the maximum increasing left side and maximum decreasing 
        # right side at the stop pos[i]
        # since left side might be all decreasing and right side might be all increasing... 
        # so the if condition during sweeping should be added.

        if len(nums) <= 3:
            return 0
        # nums = [2,1,1,5,6,2,3,1]
        n = len(nums)

        # for sure, the inc and dec dp array can be merged using one dp array... but 2 array is easier to read.... 
        inc = [0] * n
        dec = [0] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], inc[j] + 1)
        # print(inc)
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    dec[i] = max(dec[i], dec[j] + 1)
        # print(dec)
        res = 0
        for i in range(n):
         # if any one side is 0 it means it's strictly increasing (right side) or desceasing (left side) and these positions are not valid
            if inc[i] > 0 and dec[i] > 0:
                res = max(res, inc[i] + dec[i])

        return n - res - 1