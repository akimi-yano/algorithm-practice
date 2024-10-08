# 228. Summary Ranges
# Easy

# 790

# 591

# Add to List

# Share
# You are given a sorted unique integer array nums.

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b


# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
# Example 3:

# Input: nums = []
# Output: []
# Example 4:

# Input: nums = [-1]
# Output: ["-1"]
# Example 5:

# Input: nums = [0]
# Output: ["0"]

# Constraints:

# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.



# This solution works !

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        val = str(nums[0])
        prev = nums[0]

        for i in range(1, len(nums)):
            if prev + 1 == nums[i]:
                prev = nums[i]
            else:
                if int(val) == prev:
                    pass
                else:
                    val += "->" + str(prev)
                ans.append(val)
                val = str(nums[i])
                prev = nums[i]
                
        if prev + 1 != nums[-1]:
            if int(val) == prev:
                pass
            else:
                val += "->" + str(prev)
            ans.append(val) 
        
        return ans

# This solution works ! Code after code review

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        
        if not nums:
            return ans
        
        val = prev = nums[0]

        for i in range(1, len(nums)):
            if prev + 1 == nums[i]:
                prev = nums[i]
            else:
                ans.append(self.stringify(val, prev))
                val = prev = nums[i]
        ans.append(self.stringify(val, prev))
        return ans

    def stringify(self, val, prev):
        if val == prev:
            return str(val)
        return str(val) + "->" + str(prev)