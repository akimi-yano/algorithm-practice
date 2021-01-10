# 1716. Calculate Money in Leetcode Bank
# Easy

# 29

# 0

# Add to List

# Share
# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.


# Example 1:

# Input: n = 4
# Output: 10
# Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
# Example 2:

# Input: n = 10
# Output: 37
# Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
# Example 3:

# Input: n = 20
# Output: 96
# Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.


# Constraints:

# 1 <= n <= 1000


# This solution works - can still be optimized
class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        total = 0
        while n:
            for cur in range(start, start+7):
                total += cur
                n -= 1
                if n < 1:
                    return total
            start += 1
        return total


# This solution works - optimization by using div mod
class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        for day in range(n):
            #       M/T/W/Th/F/Sa/Su
            #                         week 0/1/2/...
            value = (1 + (day % 7)) + (day // 7)
            # print(f'day={day}, value={value}')
            ans += value
        return ans