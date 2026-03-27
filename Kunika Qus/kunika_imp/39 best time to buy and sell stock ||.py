# 122. Best Time to Buy and Sell Stock II

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

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
    # Time Complexity: O(2^n)
    # Space Complexity: O(n) for the recursion stack
    def helper(self, i, prices, buy):
        if i == len(prices):
            return 0

        if buy:
            profit = max(-prices[i] +self.helper(i+1, prices, 0), 0 + self.helper(i+1,prices, 1))
        else:
            profit = max(prices[i] + self.helper(i+1, prices, 1), 0 + self.helper(i+1, prices, 0))

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(0, prices, 1)
    

    # Time Complexity: O(n)
    # Space Complexity: O(n) for the dp array + O(n) for the recursion stack
    # Memoization

    def helper(self, i, prices, buy, dp):
        if i == len(prices):
            return 0

        if dp[i][buy] != -1:
            return dp[i][buy]

        if buy:
            profit = max(-prices[i] +self.helper(i+1, prices, 0, dp), 0 + self.helper(i+1,prices, 1, dp))
        else:
            profit = max(prices[i] + self.helper(i+1, prices, 1, dp), 0 + self.helper(i+1, prices, 0, dp))

        dp[i][buy] = profit
        return dp[i][buy]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for _ in range(3)] for _ in range(len(prices))]
        return self.helper(0, prices, 1, dp)
        
        