# 915. Partition Array into Disjoint Intervals
# Medium

# 805

# 47

# Add to List

# Share
# Given an array nums, partition it into two (contiguous) subarrays left and right so that:

# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

# Example 1:

# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:

# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
 

# Note:

# 2 <= nums.length <= 30000
# 0 <= nums[i] <= 106
# It is guaranteed there is at least one way to partition nums as described.

# This solution works:

from sortedcontainers import SortedList

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left = SortedList([nums[0]])
        right = SortedList(nums[1:])
        for i in range(1, len(nums)):
            if left[-1] <= right[0]:
                return i
            right.remove(nums[i])
            left.add(nums[i])
