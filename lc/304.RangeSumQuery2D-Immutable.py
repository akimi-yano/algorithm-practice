# 304. Range Sum Query 2D - Immutable
# Medium

# 1683

# 212

# Add to List

# Share
# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

# Example 1:


# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -105 <= matrix[i][j] <= 105
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion.


# This solution works:
'''
prefix sum for each row
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in range(len(matrix)):
            temp = []
            total = 0
            for col in range(len(matrix[0])):
                temp.append(total)
                total += matrix[row][col]
            temp.append(total)
            self.prefix.append(temp)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row in range(row1, row2+1):
            ans += self.prefix[row][col2+1] - self.prefix[row][col1] 
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)