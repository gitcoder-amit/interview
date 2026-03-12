# 53. Maximum Subarray


Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

'''Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104'''




class Solution:
    # Kadane's Algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        n  = len(nums)
        max_sum = -1000000
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
        n  = len(nums)
        max_sum = -1000000
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                max_sum = max(max_sum, s)
        return max_sum
