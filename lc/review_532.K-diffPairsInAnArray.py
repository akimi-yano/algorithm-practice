# 532. K-diff Pairs in an Array
# Medium

# 791

# 1468

# Add to List

# Share
# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# a <= b
# b - a == k


# Example 1:

# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:

# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# Example 4:

# Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# Output: 2
# Example 5:

# Input: nums = [-1,-2,-3], k = 1
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107




# This solution doesnt work :

# from collections import Counter
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         counts = Counter(nums)
#         ans = 0
#         # nums.sort()
#         for num in nums:
#             if num - k in counts and num - k <= num:
#                 ans += 1
#                 counts[k - num] -=1
#                 if counts[k - num] == 0:
#                     del counts[k - num]
#             if k + num in counts and num <= k + num :
#                 ans += 1
#                 counts[k + num] -=1
#                 if counts[k + num] == 0:
#                     del counts[k + num]
#         print(ans)
#         return ans
# a <= b
# b == k + a
# a == b - k 


# This solution does not work - TLED:

# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         ans = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 if nums[i] >= nums[j] and  nums[i] - nums[j] == k:
#                     ans.append((nums[j], nums[i]))
                
#                 elif nums[j] >= nums[i] and  nums[j] - nums[i] == k:
#                     ans.append((nums[i], nums[j]))
#         ans = set(ans)
#         return len(ans)


# This solution works :
# treat the case k==0 as a special case we need the count >=2 for that value to be qualified

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        if k == 0:
            total = 0
            for value in counts.values():
                if value >=2:
                    total += 1
            return total

        ans = set([])
        for num in nums:
            if num - k in counts and num - k <= num:
                ans.add((num-k,num))
                    
            if k + num in counts and num <= k + num :
                ans.add((num, num+k))
        
        return len(ans)
    
# This solution works !: optimization 
# it does not matter which is smaller or larger when its comes to diff - so just check one of them

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        if k == 0:
            total = 0
            for value in counts.values():
                if value >=2:
                    total += 1
            return total
        ans = 0
        for num in counts:
            if num - k in counts:
                ans += 1
        return ans