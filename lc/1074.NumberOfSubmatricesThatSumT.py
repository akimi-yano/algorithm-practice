# 1074. Number of Submatrices That Sum to Target
# Hard

# 1759

# 44

# Add to List

# Share
# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

# Example 1:


# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# Example 2:

# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
# Example 3:

# Input: matrix = [[904]], target = 0
# Output: 0
 

# Constraints:

# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8


# This solution works:


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        # For each row, calculate the prefix sum.
        for row in matrix:
            for i in range(COL - 1):
                row[i + 1] += row[i]
                
        res = 0
        # For each pair of columns, calculate the accumulated sum of rows.
        for i in range(COL):
            for j in range(i, COL):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1
                for k in range(ROW):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res