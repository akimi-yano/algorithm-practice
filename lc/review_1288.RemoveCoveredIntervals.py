# 1288. Remove Covered Intervals
# Medium

# 861

# 31

# Add to List

# Share
# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.

 

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1
 

# Constraints:

# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= li <= ri <= 105
# All the given intervals are unique.


# This solution works:


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        ans = 1
        max_end = intervals[0][1]
        for _, end in intervals[1:]:
            if not (end <= max_end):
                    ans += 1
            max_end = max(max_end, end)
        return ans