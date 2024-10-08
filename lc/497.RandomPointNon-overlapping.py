# 497. Random Point in Non-overlapping Rectangles

# Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

# Note:

# An integer point is a point that has integer coordinates. 
# A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.
# Example 1:

# Input: 
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output: 
# [null,[4,1],[4,1],[3,3]]
# Example 2:

# Input: 
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output: 
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# Explanation of Input Syntax:

# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.



# This solution does not work !

# import random 
# class Solution:

#     def __init__(self, rects: List[List[int]]):
#         self.rects = rects

#     def pick(self) -> List[int]:
#         i = random.randint(0,len(self.rects)-1)
#         x1,y1,x2,y2 = self.rects[i]
#         x = randint(x1,x2)
#         y = randint(y1,y2)
#         return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


# This solution works and very intuitive !

import random 
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        self.ranges = []
        rect_start = 1
        self.total_points = 0
        for rect in rects:
            self.ranges.append(rect_start)
            x1, y1, x2, y2 = rect
            num_points = (x2-x1+1) * (y2-y1+1)
            rect_start += num_points
            self.total_points += num_points
        # print(self.ranges, self.total_points)

    def pick(self) -> List[int]:
        rand = random.randint(1, self.total_points)
        rect_idx = self.helper(rand)
        x1, y1, x2, y2 = self.rects[rect_idx]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]
    
    def helper(self, pt):
        left = 0
        right = len(self.ranges) -  1
        while left < right:
            mid = (left + right + 1) // 2
            if self.ranges[mid] > pt:
                right = mid - 1
            else:
                left = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

