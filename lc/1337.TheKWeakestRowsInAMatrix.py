# 1337. The K Weakest Rows in a Matrix
# Easy

# 660

# 46

# Add to List

# Share
# Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

# A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

 

# Example 1:

# Input: mat = 
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 
# k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers for each row is: 
# row 0 -> 2 
# row 1 -> 4 
# row 2 -> 1 
# row 3 -> 2 
# row 4 -> 5 
# Rows ordered from the weakest to the strongest are [2,0,3,1,4]
# Example 2:

# Input: mat = 
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]], 
# k = 2
# Output: [0,2]
# Explanation: 
# The number of soldiers for each row is: 
# row 0 -> 1 
# row 1 -> 4 
# row 2 -> 1 
# row 3 -> 1 
# Rows ordered from the weakest to the strongest are [0,2,3,1]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 2 <= n, m <= 100
# 1 <= k <= m
# matrix[i][j] is either 0 or 1.

# This solution works:

import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        maxheap = []
        for i, row in enumerate(mat):
            heapq.heappush(maxheap, (-sum(row), -i))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        ans = []
        while maxheap:
            _, idx = heapq.heappop(maxheap)
            ans.append(-idx)
        return reversed(ans)
    '''
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
k = 3
    (2,0), (2,3) (1,2)
    '''
    
# This solution works - optimization:

import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        maxheap = []
        for i, row in enumerate(mat):
            
            left = -1
            right = len(row)-1
            while left < right:
                mid = ((left+right)+1) //2

                if row[mid] == 1:
                    left = mid
                else:
                    right = mid-1

            heapq.heappush(maxheap, (-(left+1), -i))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        ans = []
        while maxheap:
            _, idx = heapq.heappop(maxheap)
            ans.append(-idx)
        return reversed(ans)
    '''
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
k = 3
    (2,0), (2,3) (1,2)
    '''