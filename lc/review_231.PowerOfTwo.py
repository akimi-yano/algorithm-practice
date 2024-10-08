# 231. Power of Two
# Easy

# 1075

# 205

# Add to List

# Share
# Given an integer n, write a function to determine if it is a power of two.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
# Example 4:

# Input: n = 4
# Output: true
# Example 5:

# Input: n = 5
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1



# This solution works 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return (n & -n) == n
    

# This solution works 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n == n & -n


# This solution works
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0