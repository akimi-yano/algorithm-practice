# 143. Reorder List
# Medium

# 4466

# 179

# Add to List

# Share
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
 

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000


# This solution works:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        # 1) find middle
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        #    pcn
        #n 5678
# 5->n        
        # 2) reverse the latter half 
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        # 3) merge
        runner1 = head
        runner2 = prev
        while runner1 and runner2:
            runner1.next, runner2.next, runner1, runner2 = runner2, runner1.next, runner1.next, runner2.next