# 39. Combination Sum

'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

'''



class Solution:
    # Time Complexity: Exponential in nature, as in the worst case, we might explore all possible combinations. O(K*2^N) where N is the number of elements, due to the exponential number of possible combinations explored in the worst case. For each subset, it may take up to K operations to process, where K is the maximum length of any subset in the result
    # Space Complexity: O(K*N), where N is the maximum depth of recursion, which corresponds to the length of the combination path stored in memory.
    def helper(self, ans, arr, target, i, li):
        if i == len(arr):
            if target == 0:
                ans.append(li[:])
            return

        if target-arr[i] >= 0:
            li.append(arr[i])
            take = self.helper(ans, arr,target-arr[i], i, li)

            li.pop()
        not_take = self.helper(ans, arr, target, i+1, li)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.helper(ans, candidates, target, 0, [])
        return ans
        