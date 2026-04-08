# 215. Kth Largest Element in an Array

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using Sorting algorithm
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)
        nums.sort()
        return nums[len(nums)-k]

        # Using a Min Heap
        # Time Complexity: O(n log k)
        # Space Complexity: O(k)
        import heapq

        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
    

        # using a max heap
        # Time Complexity: O(n log n)
        import heapq
        max_heap = []
        for i in nums:
            heapq.heappush(max_heap, -i)

        top = -1
        while k > 0:
            top = heapq.heappop(max_heap)
            k -= 1
        
        return -top


        # using a min heap
        # Time Complexity: O(n log k)
        import heapq
        pq = []

        for i in range(k):
            heapq.heappush(pq, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, nums[i])
        
        return pq[0]
        