# 1007. Minimum Domino Rotations For Equal Row
# Medium

# 1695

# 212

# Add to List

# Share
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

 

# Example 1:


# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

# Constraints:

# 2 <= tops.length <= 2 * 104
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6


# This solution works:


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        memo = {}
        for i, num in enumerate(tops):
            if num not in memo:
                memo[num] = set([])
            memo[num].add(i)
        
        for i, num in enumerate(bottoms):
            if num not in memo:
                memo[num] = set([])
            memo[num].add(i)
        
        ans = float('inf')
        for num, arr in memo.items():
            if len(arr) == N:
                cur1 = 0
                cur2 = 0
                for i in range(N):
                    if tops[i] == num:
                        pass
                    else:
                        if bottoms[i] == num:
                            cur1 += 1
                    if bottoms[i] == num:
                        pass
                    else: 
                        if tops[i] == num:
                            cur2 += 1
                ans = min(ans, cur1, cur2)   
        return ans if ans != float('inf') else -1