# 560. Subarray Sum Equals 

'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        n = len(nums)
        c = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    c += 1
        return c

        # Optimized Approach using HashMap
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # This approach uses a hashmap to store the cumulative sum and its frequency.
        m = {}
        c = 0
        s = 0
        for i in nums:
            s += i
            if s == k:
                c += 1

            rem = s-k

            if rem in m:
                c += m[rem]

            m[s] = m.get(s, 0) + 1

        return c
            

