# 912. Sort an Array

'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104

'''


from ast import List


class Solution:
    def merge(self, a1, a2):
        temp = []
        n1, n2 = len(a1), len(a2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if a1[i] <= a2[j]:
                temp.append(a1[i])
                i += 1
            else:
                temp.append(a2[j])
                j += 1
        
        while i < n1:
            temp.append(a1[i])
            i += 1
        
        while j < n2:
            temp.append(a2[j])
            j += 1
        
        return temp

    # Time Complexity: O(nlog(n)) where n is the length of the input array
    # Space Complexity: O(n) for the temporary array used in merging
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        mid = n//2

        a1 = nums[0:mid]
        a2 = nums[mid:]

        a1 = self.sortArray(a1)
        a2 = self.sortArray(a2)

        return self.merge(a1, a2, nums)
        


class Solution:
    def merge(self, a1, a2, nums):
        temp = []
        n1, n2 = len(a1), len(a2)
        i, j, k = 0, 0, 0
        while i < n1 and j < n2:
            if a1[i] <= a2[j]:
                nums[k]=a1[i]
                i += 1
                k += 1
            else:
                nums[k] = a2[j]
                j += 1
                k += 1
        
        while i < n1:
            nums[k] = a1[i]
            k += 1
            i += 1
        
        while j < n2:
            nums[k] = a2[j]
            j += 1
            k +=1
        
        
    # Time Complexity: O(max(m,n)) where m and n are the lengths of the two subarrays
    # Space Complexity: O(1) since we are modifying the input array in place
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return

        mid = n//2

        a1 = nums[0:mid]
        a2 = nums[mid:]

        self.sortArray(a1)
        self.sortArray(a2)

        self.merge(a1, a2, nums)
        