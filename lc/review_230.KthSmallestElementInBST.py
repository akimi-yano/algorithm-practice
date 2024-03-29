# 230. Kth Smallest Element in a BST
# Medium

# 3105

# 75

# Add to List

# Share
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

# Constraints:

# The number of elements of the BST is between 1 to 10^4.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# This solution works !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.K = k
        self.target = None
        def helper(cur):
            if not cur:
                return
            helper(cur.left)
            self.K -=1 
            if self.K == 0:
                self.target = cur
                return 
            helper(cur.right)
        helper(root)
        return self.target.val