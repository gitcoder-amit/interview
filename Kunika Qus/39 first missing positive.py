# 41. First Missing Positive

'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

'''



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # T-> O(N^2) S-> O(1)
        # Brute Force
        n = len(nums)
        for i in range(1, n+1):
            if i not in nums:
                return i

        return n+1


        # T-> O(N) S-> O(N)
        # Using Extra array
        n = len(nums)
        visited = [False] * (n+1)

        for num in nums:
            if num >= 0 and num <= n:
                visited[num] = True

        for i in range(1, n+1):
            if not visited[i]:
                return i

        return n+1


        # T-> O(N) S-> O(1)
        # Optimal Approach (Index Marking)
        # 1. Replace all the negative numbers and numbers greater than n with 1.
        n = len(nums)
        contains1 = False
        for i in range(n):
            if nums[i] == 1:
                contains1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
            

        
        if not contains1:
            return 1
        
        for i in range(n):
            num = abs(nums[i])
            idx = num-1

            if nums[idx] < 0:
                continue
            else:
                nums[idx] *= -1

        
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1


        