# 62. Unique Paths


'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

'''


class Solution:
    # Time Complexity: O(2^(m+n)) Exponential
    # Space Complexity: O(m+n) Recursion stack space
    def helper(self, i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0

        up = self.helper(i-1, j)
        left = self.helper(i, j-1)

        return up + left

    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n) + O(m+n) Recursion stack space
    def helper_memo(self, i, j, dp):
        if i == 0 and j == 0:
            return 1

        if i < 0 or j  < 0 :
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.helper_memo(i-1, j, dp)
        left = self.helper_memo(i, j-1 ,dp)
        dp[i][j] = up+left
        return dp[i][j]

    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n)
    def tab_helper(self,m,n):
        dp = [[0]*(n+1) for _ in range(m+1)]

        dp[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                
                up = dp[i-1][j]
                left = dp[i][j-1]

                dp[i][j] = up+left

        return dp[m][n]


    # Time Complexity: O(m*n)
    # Space Complexity: O(n)
    def space_helper(self, m, n):
        prev = [0]*(n+1)
        for i in range(1, m+1):
            curr = [0]*(n+1)
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    curr[j] = 1
                    continue

                up = prev[j]
                left = curr[j-1]

                curr[j] = up+left

            prev = curr

        return curr[n]



    def uniquePaths(self, m: int, n: int) -> int:
        # return self.helper(m-1, n-1)

        # dp = [[-1]*n for i in range(m)]
        # return self.helper_memo(m-1, n-1, dp)

        # return self.tab_helper(m, n)
        
        return self.space_helper(m, n)
        