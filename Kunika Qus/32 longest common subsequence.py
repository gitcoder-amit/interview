class Solution:
    # Time complexity -> O(N1 * N2), Space Complexity -> O(N1*N2)
    def memo_helper(self, i1, i2, s1, s2, dp):
        if i1 < 0 or i2 < 0:
            return 0

        if dp[i1][i2] != -1:
            return dp[i1][i2]

        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + self.memo_helper(i1-1, i2-1, s1, s2, dp)
        else:
            dp[i1][i2] =  max(self.memo_helper(i1-1, i2, s1, s2, dp), self.memo_helper(i1, i2-1, s1, s2, dp)) 

        return dp[i1][i2]

    # Time Complexity -> O(2^n1 * 2^n2) , Space -> O(N+M)
    def helper(self, i1, i2, s1, s2):
        if i1 < 0 or i2 < 0:
            return 0

        
        if s1[i1] == s2[i2]:
            return 1 + self.helper(i1-1, i2-1, s1, s2)
        else:
            return max(self.helper(i1-1, i2, s1, s2), self.helper(i1, i2-1, s1, s2))
        
        return max(take, not_take)

    # T -> O(N1 * N2), S -> O(N*M) + O(N+M)
    def tab_helper(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i1 in range(n1+1):
            dp[i1][0] = 0

        for i2 in range(n2+1):
            dp[0][i2] = 0
        
        for i1 in range(1, n1+1):
            for i2 in range(1,  n2+1):
                if s1[i1-1] == s2[i2-1]:
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])

        return dp[n1][n2], dp

    
    # T -> O(N*M) S -> (N+M)
    def space_helper(self, s1, s2):
        n = len(s1)
        m = len(s2)

        prev = [0]*(m+1)
        cur = [0]*(m+1)

        for i1 in range(1, n+1):
            for i2 in range(1, m+1):
                if s1[i1-1] == s2[i2-1]:
                    cur[i2] = 1 + prev[i2-1]
                else:
                    cur[i2] = max(prev[i2], cur[i2-1])
        
            prev = cur[:]
        
        return prev[m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        return self.helper(n1-1, n2-1, text1, text2)


        # n1 = len(text1)
        # n2 = len(text2)
        # dp = [[-1]*n2 for _ in range(n1)]

        # return self.memo_helper(n1-1, n2-1, text1, text2, dp)

        # ans, dp = self.tab_helper(text1, text2)
        # print(dp)
        # return ans

        # ans = self.space_helper(text1, text2)
        # return ans
        