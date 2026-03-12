# 347. Top K Frequent Elements

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using Sorting
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1

        
        map_items = m.items()
        sorted_map_items = sorted(map_items, key = lambda x : x[1], reverse = True)
        
        ans = []
        for i in range(k):
            ans.append(sorted_map_items[i][0])

        return ans
            


        ## Using a Min Heap
        # # Time Complexity: O(n log k)
        ## Space Complexity: O(n)
        import heapq
        m  = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1


        heap = []
        for num, freq in m.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        result = []
        while heap:
            req_value = heapq.heappop(heap)[1]
            result.append(req_value)

        return result


