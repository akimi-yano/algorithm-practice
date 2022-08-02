# 378. Kth Smallest Element in a Sorted Matrix
# Medium

# 6833

# 252

# Add to List

# Share
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2
 

# Follow up:

# Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
# Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.


# This solution works:


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, left, right = len(matrix), matrix[0][0], matrix[-1][-1]
        
        def check(m):
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > m: j -= 1
                cnt += (j + 1)
            return cnt
         
        while left < right:
            mid = (left + right)//2
            if check(mid) < k:
                left = mid + 1
            else:
                right = mid
                
        return left

'''
The idea is for number X find number of elements which are less or equal than X, which can be done in O(n), idea is similar to problem 240: Search a 2D Matrix II: we can start with the top right element and move only down and to the left, counting number of elements <X in each row. We start with the smallest and the biggest elements in our table and do binary search, each time asking question: is number of elements < X is more than k? We do binary search and stop when end become equal to beg.

Complexity
Time complexity is O(n * log(A)), where A is difference between maximum and minimum values in our matrix.
'''