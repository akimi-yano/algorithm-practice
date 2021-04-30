# 48. Rotate Image
# Medium

# 4821

# 337

# Add to List

# Share
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# Example 3:

# Input: matrix = [[1]]
# Output: [[1]]
# Example 4:

# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
 

# Constraints:

# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# This solution works:
'''
transpose (each col starts with the row) and flip left and right
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for row in range(N):
            for col in range(row, N):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                
        for row in range(N):
            for col in range(N//2):
                matrix[row][col],matrix[row][N-1-col] = matrix[row][N-1-col],matrix[row][col]

    
# This solution works:
'''
flipping the corners first - 4 points and move right and inside
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        r = 0
        c_start = 0
        c_end = N - 2
        while c_start <= c_end:
            for c in range(c_start, c_end + 1):
                # rotate 4 tiles
                matrix[r][c],matrix[c][N-1-r],matrix[N-1-r][N-1-c],matrix[N-1-c][r]=matrix[N-1-c][r],matrix[r][c],matrix[c][N-1-r],matrix[N-1-r][N-1-c]
            r += 1
            c_start += 1
            c_end -= 1