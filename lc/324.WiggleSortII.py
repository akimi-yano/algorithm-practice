# 324. Wiggle Sort II

# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

# Example 1:

# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# Example 2:

# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# Note:
# You may assume all input has valid answer.

# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?





# This solution does not work:

# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         temp = []
#         for i in range(len(nums)):
#             temp.append(nums[i])
#         temp.sort()
#         # print(temp)
#         i = 0
#         if len(temp)%2!=0:
#             odd = 1
#         else:
#             odd = 0
#         for k in range(len(temp)):
#             if k%2 == 0:
#                 nums[k] = temp[k-i]
#             else:
#                 # nums[k] = temp[len(temp)-k+i]
#                 nums[k] = temp[len(temp)//2+odd+i]
#                 i+=1
                
# #         0 1 2 3 4 5
# #         1 6  15  14
# #         1 len(temp)=6 - 0 - 6
# #         3 len(temp)=6 - 1 - 5
# #         5 len(temp)=6 - 2 - 4
        
# #         1 - 0 - k-1
# #         3 - 1 - k-2
# #         5 - 2 - k-3
            
# '''
# Example 1:
# Input:  [1, 5, 1, 1, 6, 4]
# Output: [1, 4, 1, 5, 1, 6].

# Example 2:
# Input:  [1, 3, 2, 2, 3, 1]
# Output: [2, 3, 1, 3, 1, 2].
# '''




# This solution works!



# Downside is it is O(n*logn) and O(N) space but it is the simplest solution.

# Just put sorted numbers in array
# Put largest numbers in odd indexes first
# Then put remaining numbers in even indexes
# So even < odd > even
class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        for i in range(1, len(nums), 2): 
            nums[i] = arr.pop() 
        for i in range(0, len(nums), 2): 
            nums[i] = arr.pop() 
        

# Its sorted - so you put large ones to the odd index by popping the elem from array
# and then you put smaller ones to the even index by popping the rest of elem from array



# another solution !
# Python, deterministic O(n) time + O(1) memory, quick select + "median of medians"
# not completely deterministic of O(N) 
# deterministic : you get the same result everytime you implement it 

'''
Basic idea: we find median value, put numbers bigger than median into odd index, smaller than median into even index.
Naive solution:

Sort the array to find median in O(nlgn) time + O(1) space
Move odd and even index numbers into temp array and move them back to the original array with new index. Taking O(n) time + O(n) space.
Total: O(nlgn) time + O(n) space
In order to achieve O(n) time + O(1) space, we need to answer two questions:

How to find median in O(n)+O(1)
How to re-order the odd-even indexes "in-place" using O(1) memory.
Three knowledge pre-requisitions:

Quick select to find median in O(n) time on average, O(n^2) in worst case. Taking O(1) memory.
"Median of medians" alogrithm to improve quick select, making the time complexity "deterministic O(n)" rather than "average O(n)".
Virtual indexing technology to achieve in-place wiggle sort based on median value found above.
There is "median of medians + quick select" methods provided out of the box in all languages. You have to write it yourself.
This problem deserve to be of "Hard" difficulty rather than "Medium" for the O(n)+O(1) solution, considering so many technologies involved.

Virtual index:
This is actually a "Three color Sort" problem. Imagine scanning the nums this way: "1,3,5,7,9, ... 0,2,4,6,8,10...". During the scan, when you see a big number, put it to "left", a small number, put it to "right", in the end, you will see all big numbers on left, all small numbers on right, and all median numbers in the middle.
But wait, here "left" and "right" are actually the left and right of "1,3,5,7...0,2,4,6,8,..." indexes, not the left and right of "0,1,2,3,4,5...", because you are scanning in "1,3,5,7...0,2,4,6,8,..." order. So what you actually see is all big numbers on odd index, all small numbers on even index, all median numbers distributed on the left and right side of the array. And this kind of distribution is guaranteed to be wiggled sorted.

Code:
I use random pivot for quick select rather than "median of medians", which is much easier to implement and has average O(n) for all kind of input pattern.
Please be noted that you cannot use recursion in the fast select part, otherwise the space complexity won't be real O(1).
'''

import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def nsmallest(nums,n):            
            start,end=0,len(nums)-1
            while True:
                pivot=nums[random.randint(start,end)]
                i,j,k=start,end,start
                while k<=j:
                    if nums[k]<pivot:
                        nums[i],nums[k]=nums[k],nums[i]
                        i+=1
                        k+=1
                    elif nums[k]>pivot:
                        nums[j],nums[k]=nums[k],nums[j]
                        j-=1
                    else:
                        k+=1
                if i<=n-1<=j:
                    return pivot
                elif n-1<i:
                    end=i-1
                else:
                    start=i+1
        n=len(nums)
        mid=nsmallest(nums,(n+1)//2)
        mapIdx=lambda i:(1+2*i)%(n|1)
        i,j,k=0,n-1,0
        while k<=j:
            if nums[mapIdx(k)]>mid:
                nums[mapIdx(k)],nums[mapIdx(i)]=nums[mapIdx(i)],nums[mapIdx(k)]
                i+=1
                k+=1
            elif nums[mapIdx(k)]<mid:
                nums[mapIdx(k)],nums[mapIdx(j)]=nums[mapIdx(j)],nums[mapIdx(k)]
                j-=1
            else:
                k+=1