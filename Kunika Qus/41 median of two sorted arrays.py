'''
4. Median of Two Sorted Arrays
Solved
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''


class Solution:
    # Time Complexity: O((n1+n2)
    # Space Complexity: O(n1+n2)
    def median(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        merged = []
        i, j = 0, 0
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        while i < n1:
            merged.append(arr1[i])
            i += 1
        
        while j < n2:
            merged.append(arr2[j])

        n = n1+n2

        if n%2 == 1:
            return float(merged[n//2])
        
        return (merged[n//2] + merged[(n//2)-1])/2

    # Better Approach:
    # Time Complexity: O(n1+n2)
    # Space Complexity: O(1)
    def median(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        count = 0
        ele1, ele2 = -1, -1
        n = n1+n2
        ind2 = n//2
        ind1 = ind2 - 1
        i, j = 0, 0
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                if count == ind1:
                    ele1 = arr1[i]
                if count == ind2:
                    ele2 = arr1[i]
                i += 1
                count += 1
            else:
                if count == ind1:
                    ele1 = arr2[j]
                if count == ind2:
                    ele2 = arr2[j]
                j += 1
                count += 1
            
        while i < n1:
            if count  == ind1:
                ele1 = arr1[i]
            if count == ind2:
                ele2 = arr1[i]
            count += 1
            i += 1
        
        while j < n2:
            if count == ind1:
                ele1 = arr2[j]
            if count == ind2:
                ele2 = arr2[j]
            count += 1
            j += 1
        
        if n%2 == 0:
            return (ele1+ele2)/2
        else:
            return float(ele2)
            

    # Optimal Approach: Binary Search Remaining  check from striver
        
