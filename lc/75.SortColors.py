# 75. Sort Colors
# Medium

# 7198

# 348

# Add to List

# Share
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:

# Input: nums = [0]
# Output: [0]
# Example 4:

# Input: nums = [1]
# Output: [1]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


# This solution works:


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = ones = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
                
        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
