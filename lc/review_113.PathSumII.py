# 113. Path Sum II
# Medium

# 3376

# 92

# Add to List

# Share
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def helper(cur, remaining, arr):
            
            if not cur:
                return
            if not cur.left and not cur.right:
                if remaining - cur.val == 0:
                    ans.append(arr+[cur.val])
                return
            
            helper(cur.left, remaining - cur.val, arr + [cur.val])
            helper(cur.right, remaining - cur.val, arr + [cur.val])
            
        ans = []
        helper(root, targetSum, [])
        return ans