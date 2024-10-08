# 852. Peak Index in a Mountain Array
# Easy

# 982

# 1348

# Add to List

# Share
# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

# Example 1:

# Input: arr = [0,1,0]
# Output: 1
# Example 2:

# Input: arr = [0,2,1,0]
# Output: 1
# Example 3:

# Input: arr = [0,10,5,2]
# Output: 1
# Example 4:

# Input: arr = [3,4,5,1]
# Output: 2
# Example 5:

# Input: arr = [24,69,100,99,79,78,67,36,26,19]
# Output: 2
 

# Constraints:

# 3 <= arr.length <= 104
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.
 

# Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?


# This solution works - Time: O(N)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        val = max(arr)
        i = arr.index(val)
        return i
    
# This solution works - optimiation - Time: O(log(N))

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l <= r:
            m = (l+r) // 2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m-1] > arr[m]:
                r = m -1
            elif arr[m] < arr[m+1]:
                l = m + 1
        return l