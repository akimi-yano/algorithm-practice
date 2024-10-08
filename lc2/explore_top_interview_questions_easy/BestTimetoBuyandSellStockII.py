'''
122. Best Time to Buy and Sell Stock II
Medium
11.2K
2.5K
Companies
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        has_stock
        true -> cannot buy & can sell
        false -> can buy & cannot sell
        '''
        @lru_cache()
        def helper(has_stock, i):
            if i > len(prices)-1:
                return 0
            best = 0
            if has_stock:
                best = max(best, prices[i]+helper(False,i+1), helper(has_stock,i+1))
            else:
                best = max(best, -prices[i]+helper(True,i+1), helper(has_stock,i+1))
            return best
        return helper(False, 0)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        ans = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                ans += (prices[i] - prices[i-1])
        return ans