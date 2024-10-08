# 174. Dungeon Game
# Hard

# 2956

# 61

# Add to List

# Share
# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Return the knight's minimum initial health so that he can rescue the princess.

# Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

# Example 1:


# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7
# Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
# Example 2:

# Input: dungeon = [[0]]
# Output: 1
 

# Constraints:

# m == dungeon.length
# n == dungeon[i].length
# 1 <= m, n <= 200
# -1000 <= dungeon[i][j] <= 1000


# This solution works:

'''
Probably when you see this problem and you have some experience in this type of problems you can guess, that this is dynamic programming problem. However even if you understand this, it is not easy to solve it. Let us use top-down dp, that is Let dp[i][j] be the minimum hp we need to reach the princess if we start from point (i,j). Let us consider the following example:

-2	-3	+3
-5	-10	+1
+10	+30	-5
Let us add bottom dummy row and right dummy column to handle border cases more easy. We fill it with infinities, except two ones - neibours of our princess. I will explain it a bit later.

How we can evaluate dp[i][j]? We need to look at two cells: dp[i+1][j] and dp[i][j+1] and evaluate two possible candidates: dp[i+1][j]-dungeon[i][j] and dp[i][j+1]-dungeon[i][j].

If at least one of these two numbers is negative, it means that we can survive just with 1 hp: (look at number +30 in our table for example)
If both this numbers are positive, we need to take the mimumum of them, see for example number -10 in our table: to survive we need either 5- -10 = 15 if we go right and 1- -10 = 11 if we go down, of course we choose 11.
This conditions can be written in one a bit ugly line: dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1).
Finally, why I put 1 to two neibors of princess? To make this formula valid for princess cell: if we have negative number like -5 in this cell, we need 6 hp to survive, if we have non-negative number in this cell, we need 1 hp to survive.
7	5	2	inf
6	11	5	inf
1	1	6	1
inf	inf	1	#
Complexity: both time and space is O(mn). Space complexity can be reduced to O(min(m,n)) as usual, because we look only to neibour cells. However code becomes a bit more difficult to follow.
'''

class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]