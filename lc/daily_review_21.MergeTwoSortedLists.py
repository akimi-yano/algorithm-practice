# 21. Merge Two Sorted Lists
# Easy

# 5749

# 697

# Add to List

# Share
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

# Example 1:


# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: l1 = [], l2 = []
# Output: []
# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.


# This solution works !

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(cur1, cur2):
            if not cur1:
                return cur2
            elif not cur2:
                return cur1
            elif cur1.val < cur2.val:
                cur1.next = helper(cur1.next, cur2)
                return cur1
            else:
                cur2.next = helper(cur1, cur2.next)
                return cur2
            
        return helper(l1, l2)