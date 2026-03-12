# 15. 3Sum

'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105 '''



class Solution:
    # T -> O(nlogn + n^3)
    # Space -> O(n) for storing the triplets
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]

                        if triplet not in ans:
                            ans.append(triplet)

        return ans



        # T -> O(n^2) + # O(nlogn) for sorting
        # Space -> O(n) for storing the triplets + # O(n) for the hashmap
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n):
            m = {}
            for j in range(i+1, n):
                third = -(nums[i] + nums[j])
                if third in m:
                    triplet = [nums[i],nums[j], third]
                    if triplet not in ans:
                        ans.append(triplet)
                else:
                    m[nums[j]] = True

        return ans

        # T -> O(n^2) + O(nlogn) for sorting
        # Space -> O(n) for storing the triplets
        # Two Pointer Approach
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if  s == 0:
                    triplet = [nums[i],nums[j], nums[k]]
                    ans.append(triplet)
                    j += 1
                    k -= 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return ans

        