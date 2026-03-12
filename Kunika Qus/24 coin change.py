# 322. Coin Change

'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

'''

class Solution:
    import sys
    def helper(self, arr, target, i):
        if i == 0:
            if target % arr[0] == 0:
                return target // arr[0]
            return sys.maxsize

        
        take = sys.maxsize
        if arr[i] <= target:
            take = self.helper(arr, target-arr[i], i) + 1
        not_take = self.helper(arr, target, i-1)
        return min(take, not_take)

    def helper_memo(self, arr, target, i, dp):
        if i == 0:
            if target % arr[i] == 0:
                return target // arr[i]
            return sys.maxsize

        if dp[i][target] != -1:
            return dp[i][target]

        take = sys.maxsize
        if arr[i] <= target:
            take = self.helper_memo(arr, target-arr[i], i, dp) + 1
        not_take = self.helper_memo(arr, target, i-1, dp)
        dp[i][target] = min(take, not_take)
        return dp[i][target]


    def coinChange(self, coins: List[int], amount: int) -> int:
        # n = len(coins)
        # ans = self.helper(coins, amount, n-1)

        # if ans == sys.maxsize:
        #     return -1
        
        # return ans

        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        ans = self.helper_memo(coins, amount, n-1, dp)

        if ans == sys.maxsize:
            return -1
        
        return ans