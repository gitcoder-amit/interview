# 209. Minimum Size Subarray Sum

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

'''

class Solution:
    # T -> O(n^2) S -> O(1)
    # Brute Force
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = 10000000000
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s >= target:
                    min_len = min(min_len, j-i+1)
        return min_len if min_len != 10000000000 else 0



    # T -> O(n) S -> O(1)
    # Optimal Approach (Two Pointer)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        
        l, r = 0, 0
        s = 0
        min_len = 1000000000000
        while r < n:
            s += nums[r]
            
            while s >= target:
                min_len = min(min_len, r-l+1)
                s -= nums[l]
                l += 1
                
            
            r += 1
        return min_len if min_len != 1000000000000 else 0

        