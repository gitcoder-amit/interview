# 152. Maximum Product Subarray


'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute force approach
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        max_product = float('-inf')
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                max_product = max(max_product, product)
        return max_product



       # kadane algorithm for maximum product subarray
       # Time Complexity: O(n)
       # Space Complexity: O(1)
    # Initialize variables to track max and min products ending at current position
        max_prod = nums[0]
        min_prod = nums[0]
        result = max_prod
        
        for i in range(1, len(nums)):
            # To handle negative numbers, we swap max and min when encountering a negative number
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            
            # Update max and min products for current position
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            
            # Update the global maximum product found so far
            result = max(result, max_prod)
        
        return result


        # Observations Aproach
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        pref = 1
        suff = 1
        max_product = float('-inf')
        for i in range(len(nums)):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            pref *= nums[i]
            suff *= nums[len(nums) - 1 - i]
            max_product = max(max_product, pref, suff)
            
            