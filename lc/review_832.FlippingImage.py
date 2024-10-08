# 832. Flipping an Image
# Easy

# 1071

# 165

# Add to List

# Share
# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example 1:

# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:

# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Notes:

# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1


# This solution works !


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ROW = len(A)
        COL = len(A[0])
        
        for row in range(ROW):
            for col in range(COL//2):
                A[row][col], A[row][COL-1-col] = A[row][COL-1-col], A[row][col]
        
        for row in range(ROW):
            for col in range(COL):
                A[row][col] ^= 1
                
        return A
    


# This solution works ! - 1 liner


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[col^1 for col in reversed(row)] for row in A]