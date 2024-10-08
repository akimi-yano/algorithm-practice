# 235. Lowest Common Ancestor of a Binary Search Tree
# Easy

# 3629

# 146

# Add to List

# Share
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.


# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':   
        def helper(cur, look_val):
            if cur.val == look_val:
                return [cur]
            elif cur.val < look_val:
                arr = helper(cur.right, look_val)
                arr.append(cur)
                return arr
            elif cur.val > look_val:
                arr = helper(cur.left, look_val)
                arr.append(cur)
                return arr
            else:
                print("THIS SHOULD NOT HAPPEN")
            
        
        p_path = helper(root, p.val)
        p_path.reverse()
        q_path = helper(root, q.val)
        q_path.reverse()
        # print(p_path[-1].val, q_path[-1].val)
        prev = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i].val == q_path[i].val:
                prev = p_path[i]
            else:
                return prev
        return prev