# 2. Add Two Numbers
# Medium

# 16824

# 3583

# Add to List

# Share
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# This solution works:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0
        newhead = None
        while cur1 and cur2:
            carry, val = divmod(cur1.val+cur2.val+carry, 10)
            if newhead is None:
                cur = newhead = ListNode(val)
            else:
                cur.next = ListNode(val)
                cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
                
        while cur1:
            carry, val = divmod(cur1.val+carry, 10)
            if newhead is None:
                cur = newhead = ListNode(val)
            else:
                cur.next = ListNode(val)
                cur = cur.next
            cur1 = cur1.next
        
        while cur2:
            carry, val = divmod(cur2.val+carry, 10)
            if newhead is None:
                cur = newhead = ListNode(val)
            else:
                cur.next = ListNode(val)
                cur = cur.next
            cur2 = cur2.next
        
        if carry:
            cur.next = ListNode(carry)
            
        return newhead
            