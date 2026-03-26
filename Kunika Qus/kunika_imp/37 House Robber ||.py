# 213. House Robber II

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''


class Solution:
    def helper(self, nums, i, dp):
        if i == 0:
            return nums[0]
        
        if i == 1:
            return max(nums[0], nums[1])

        if dp[i] != -1:
            return dp[i]

        take = self.helper(nums, i-2, dp) + nums[i]
        not_take = self.helper(nums, i-1, dp) + 0

        dp[i] = max(take, not_take) 
        return dp[i]

    def f(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return self.helper(nums, len(nums)-1, dp)
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        temp1 = []
        temp2 = []
       
        for i in range(n):
            if i != 0:
                temp1.append(nums[i])
            if i != n-1:
                temp2.append(nums[i])
            

        return max(self.f(temp1), self.f(temp2)) 

        