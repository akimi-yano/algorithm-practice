'''
172. Factorial Trailing Zeroes
Solved
Medium
Topics
Companies
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?
'''

# This solution works:

class Solution:
    def trailingZeroes(self, n: int) -> int:
        bosuu = 5
        ans = 0
        while bosuu <= n:
            ans += n // bosuu
            bosuu *= 5
        return ans

# Time: O(log5N)
# Space: O(1)