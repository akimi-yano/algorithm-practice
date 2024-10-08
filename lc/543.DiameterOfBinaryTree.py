# 543. Diameter of Binary Tree
# Easy

# 5981

# 370

# Add to List

# Share
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_length(cur):
            nonlocal longest
            if not cur:
                return 0
            left = right = 0
            if cur.left:
                left = 1 + get_length(cur.left)
            if cur.right:
                right = 1 + get_length(cur.right)
            longest = max(longest, left + right)
            return max(left, right)
        
        longest = 0
        get_length(root)
        return longest
