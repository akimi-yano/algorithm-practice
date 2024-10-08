# 1539. Kth Missing Positive Number
# Easy

# 596

# 19

# Add to List

# Share
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Find the kth positive integer that is missing from this array.

 

# Example 1:

# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
# Example 2:

# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

# Constraints:

# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length

# This solution works !

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = set(arr)
        for i in range(1, 2001):
            if i not in nums:
                k -= 1
                if k == 0:
                    return i


# This solution works ! - Optimization - Constant space
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        # k = 200
        # arr = [100,...]

        for cur in arr:
            if prev + k < cur:
                break
            skipped = cur - prev - 1
            k -= skipped
            prev = cur
        return prev + k
        