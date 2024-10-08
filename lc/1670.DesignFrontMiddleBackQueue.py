# 1670. Design Front Middle Back Queue
# Medium

# 29

# 9

# Add to List

# Share
# Design a queue that supports push and pop operations in the front, middle, and back.

# Implement the FrontMiddleBack class:

# FrontMiddleBack() Initializes the queue.
# void pushFront(int val) Adds val to the front of the queue.
# void pushMiddle(int val) Adds val to the middle of the queue.
# void pushBack(int val) Adds val to the back of the queue.
# int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
# int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
# int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
# Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

# Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
# Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
 

# Example 1:

# Input:
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# Output:
# [null, null, null, null, null, 1, 3, 4, 2, -1]

# Explanation:
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // return 1 -> [4, 3, 2]
# q.popMiddle();    // return 3 -> [4, 2]
# q.popMiddle();    // return 4 -> [2]
# q.popBack();      // return 2 -> []
# q.popFront();     // return -1 -> [] (The queue is empty)
 

# Constraints:

# 1 <= val <= 109
# At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.

# This approach works ! - 1 liners with stack:

class FrontMiddleBackQueue:

    def __init__(self):
        self.A = []
        
    def pushFront(self, val: int) -> None:
        self.A.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.A.insert(len(self.A)//2, val)

    def pushBack(self, val: int) -> None:
        self.A.append(val)
        
    def popFront(self) -> int:
        return (self.A or [-1]).pop(0)
        
    def popMiddle(self) -> int:
        return (self.A or [-1]).pop((len(self.A) - 1) // 2)
    
    def popBack(self) -> int:
        return (self.A or [-1]).pop()
        

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()


# This approach works - faster:
    
from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.A = deque()
        self.B = deque()

    def pushFront(self, val):
        self.A.appendleft(val)
        self.balance()

    def pushMiddle(self, val):
        if len(self.A) > len(self.B):
            self.B.appendleft(self.A.pop())
        self.A.append(val)

    def pushBack(self, val):
        self.B.append(val)
        self.balance()

    def popFront(self):
        val = self.A.popleft() if self.A else -1
        self.balance()
        return val

    def popMiddle(self):
        val = (self.A or [-1]).pop()
        self.balance()
        return val

    def popBack(self):
        val = (self.B or self.A or [-1]).pop()
        self.balance()
        return val

    # keep A.size() >= B.size()
    def balance(self):
        if len(self.A) > len(self.B) + 1:
            self.B.appendleft(self.A.pop())
        if len(self.A) < len(self.B):
            self.A.append(self.B.popleft())
        

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()



# This approach does not work:

'''
it is important to decide if we want to keep the extra in the left queue or right queue
also know when we want to call self.fix/ balance()
'''
    
# from collections import deque
# class FrontMiddleBackQueue:

#     def __init__(self):
#         self.left = deque([])
#         self.right = deque([])
        
#     def pushFront(self, val: int) -> None:
#         self.left.appendleft(val)
#         self.fix()

#     def pushMiddle(self, val: int) -> None:
#         if len(self.left) == len(self.right):
#             self.right.appendleft(val)
#         elif len(self.left) +1 == len(self.right):
#             self.left.append(val)
#         self.fix()

#     def pushBack(self, val: int) -> None:
#         self.right.append(val)
#         self.fix()
        
#     def popFront(self) -> int:
#         if not self.left and not self.right:
#             return -1
#         self.fix()
#         popped = -1
#         if self.left:
#             popped = self.left.popleft()
#             self.fix()
#         return popped
        
#     def popMiddle(self) -> int:
#         if not self.left and not self.right:
#             return -1
#             self.fix()
#         popped = -1
#         if len(self.left) == len(self.right) and self.left:
#             popped = self.left.pop() 
#         elif len(self.left) + 1 == len(self.right) and self.right:
#             popped = self.right.popleft()
#         self.fix()
#         return popped
    
#     def popBack(self) -> int:
#         if not self.left and not self.right:
#             return -1
#         self.fix()
#         popped = -1
#         if self.right:
#             popped = self.right.pop() 
#             self.fix()
#         return popped
    
#     def fix(self):
#         while len(self.left) > len(self.right):
#             popped = self.left.pop()
#             self.right.appendleft(popped)
#             self.fix()
        
#         while len(self.left) + 1 < len(self.right):
#             popped = self.right.popleft()
#             self.left.append(popped)
#             self.fix()
        

# # Your FrontMiddleBackQueue object will be instantiated and called as such:
# # obj = FrontMiddleBackQueue()
# # obj.pushFront(val)
# # obj.pushMiddle(val)
# # obj.pushBack(val)
# # param_4 = obj.popFront()
# # param_5 = obj.popMiddle()
# # param_6 = obj.popBack()