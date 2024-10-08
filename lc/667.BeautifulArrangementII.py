# 667. Beautiful Arrangement II
# Medium

# 506

# 831

# Add to List

# Share
# Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
# Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

# If there are multiple answers, print any of them.

# Example 1:
# Input: n = 3, k = 1
# Output: [1, 2, 3]
# Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
# Example 2:
# Input: n = 3, k = 2
# Output: [1, 3, 2]
# Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
# Note:
# The n and k are in the range 1 <= k < n <= 104.

# This solution works:

class Solution:
    '''
    n = 10
    k = 3
      +3   -2   +1
    1 -> 4 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    
    k = 10
      +10   -9   +8    -7   +6   -5   +4   -3   +2   -1
    1 -> 11 -> 2 -> 10 -> 3 -> 9 -> 4 -> 8 -> 5 -> 7 -> 6
    
    '''
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [1]
        diff = k
        multiplier = 1
        while diff > 0:
            prev = ans[-1]
            cur = prev + (diff * multiplier)
            ans.append(cur)
            diff -= 1
            multiplier *= -1
        
        prev = 1 + k
        
        while len(ans) < n:
            ans.append(prev + 1)
            prev += 1
        return ans