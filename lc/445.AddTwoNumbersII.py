# 445. Add Two Numbers II
# Medium

# 1821

# 177

# Add to List

# Share
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# This solution works !
'''
so many edge cases and long code but I cannot miss any edge cases to make this code work  !
idea is reverse sll1 and sll2 and do summation while making new ListNode  and then reverse  again  before returning
do addition including carry 
also  check carry one more time before return
do the merging part like merge 2 sorted arrays
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rl1 =self.reverse(l1)
        rl2 =self.reverse(l2)
        cur1 = rl1
        cur2 = rl2
        head = None
        carry = 0
        
        while cur1 and cur2:  
            addition = cur1.val + cur2.val + carry
            value = addition % 10
            
            if not head:
                head = ListNode(value)
                cur = head
            else:
                cur.next = ListNode(value) 
                cur = cur.next
            carry = addition // 10
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1:  
            addition = cur1.val +carry
            value = addition % 10
            
            if not head:
                head = ListNode(value)
                cur = head
            else:
                cur.next = ListNode(value) 
                cur = cur.next
            carry = addition // 10
            cur1 = cur1.next
        
        while cur2:  
            addition = cur2.val + carry
            value = addition % 10
            
            if not head:
                head = ListNode(value)
                cur = head
            else:
                cur.next = ListNode(value)
                cur = cur.next
            carry = addition // 10
            cur2 = cur2.next
        
        if carry:
            cur.next = ListNode(carry)
        
        return self.reverse(head)
        '''
        7->2->4->3->x
        x<-7<-2<-4<-3
        3->4->2->7->x
        
                      prev cur next_node
        None<-7-<-2<-4<-3 
        ''' 
    
    def reverse(self, head):
        cur = head 
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        head = prev
        return head
        
        
# This solution works too:
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        a1, a2 = [], []
        while l1:
            a1.append(l1.val)
            l1 = l1.next
        while l2:
            a2.append(l2.val)
            l2 = l2.next  
        
        nxt, carry = None, 0
        while a1 or a2 or carry:
            val = carry
            if a1:
                val += a1.pop()
            if a2:
                val += a2.pop()
            val, carry = val % 10, val // 10
            nxt = ListNode(val, nxt)
        return nxt 
    

# This solution works ! little oprimized !

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        rl1 =self.reverse(l1)
        rl2 =self.reverse(l2)
        cur1 = rl1
        cur2 = rl2
        val, carry = (cur1.val + cur2.val) % 10, (cur1.val + cur2.val) // 10
        cur = head = ListNode(val)
        cur1, cur2 = cur1.next, cur2.next
        
        while cur1 or cur2 or carry:  
            addition = carry
            if cur1:
                addition += cur1.val
                cur1 = cur1.next
            if cur2:
                addition += cur2.val
                cur2 = cur2.next
            value = addition % 10
            cur.next = ListNode(value) 
            cur = cur.next
            carry = addition // 10
        
        return self.reverse(head)
    
    def reverse(self, head):
        cur = head 
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        head = prev
        return head
        
    