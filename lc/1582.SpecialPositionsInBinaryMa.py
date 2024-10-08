# 1582. Special Positions in a Binary Matrix
# Easy

# 26

# 3

# Add to List

# Share
# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

# A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:

# Input: mat = [[1,0,0],
#               [0,0,1],
#               [1,0,0]]
# Output: 1
# Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:

# Input: mat = [[1,0,0],
#               [0,1,0],
#               [0,0,1]]
# Output: 3
# Explanation: (0,0), (1,1) and (2,2) are special positions. 
# Example 3:

# Input: mat = [[0,0,0,1],
#               [1,0,0,0],
#               [0,1,1,0],
#               [0,0,0,0]]
# Output: 2
# Example 4:

# Input: mat = [[0,0,0,0,0],
#               [1,0,0,0,0],
#               [0,1,0,0,0],
#               [0,0,1,0,0],
#               [0,0,0,1,1]]
# Output: 3
 

# Constraints:

# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is 0 or 1.


# This solution works:

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        '''
        ones = [(0,0)]
     
        rows{0:1}
        cols{0:}
        '''
        if not mat or not mat[0]:
            return 0
        m = len(mat)
        n = len(mat[0])
        ones = set([])
        for row in range(m):
            for col in range(n):
                if mat[row][col]==1:
                    ones.add((row,col))
        # print(ones)
        rows = {}
        cols = {}
        for row, col in ones:
            if row not in rows:
                rows[row] = 1
            else:
                rows[row] += 1
            if col not in cols:
                cols[col] = 1
            else:
                cols[col] += 1
        ans = 0        
        # print(rows,cols)
        for row,r_count in rows.items():
            for col, c_count in cols.items():
                if r_count ==1 and c_count ==1 and (row,col) in ones:
                    ans+=1
        return ans 
        
            