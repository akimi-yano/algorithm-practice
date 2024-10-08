# 326. Power of Three
# Easy

# 1311

# 146

# Add to List

# Share
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Example 2:

# Input: n = 0
# Output: false
# Example 3:

# Input: n = 9
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?


# This solution works:


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%3 == 0:
            return self.isPowerOfThree(n//3)
        return False
        
            