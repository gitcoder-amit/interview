# 128. Longest Consecutive Sequence

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''



class Solution:
    # Time Complexity: O(nlogn) due to sorting the array.
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        maxlen = 1
        c = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                c += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                c = 1
            maxlen = max(maxlen, c)
        return maxlen

    # Need to check time complexity Time Complexity: O(n) due to the use of a set for lookups. 
    '''Line Number 66 Checking if num-1 in nums on a list would indeed take O(n) for each check.

    Then the whole loop would degrade to O(n²).
    That’s exactly why the first line converts the list into a set. 
    (x in set) is O(1) on average (amortized).

    It only becomes worse if you had lots of hash collisions, but that’s rare in practice.'''
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxlen = 0

        for num in num_set:  
            if num-1 not in num_set:
                c = 1
                current_num = num

                while current_num + 1 in num_set:
                    c += 1
                    current_num += 1

                maxlen = max(maxlen, c)
        return maxlen
        