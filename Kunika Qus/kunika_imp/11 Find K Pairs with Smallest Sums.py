'''
373. Find K Pairs with Smallest Sums


You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length


'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        pq = []
        n1, n2 = len(nums1), len(nums2)
        for i in range(min(n1, k)):
            for j in range(min(n2, k)):
                sum_pair = nums1[i] + nums2[j]
                heapq.heappush(pq, (sum_pair, nums1[i], nums2[j]))
        
        ans = []
        for _ in range(min(k, len(pq))):
            ele = heapq.heappop(pq)
            ans.append([ele[1], ele[2]])
        
        return ans
    
    # Better Approach
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        pq = []
        n1, n2 = len(nums1), len(nums2)
        for i in range(min(n1, k)):
            sum_pair = nums1[i] + nums2[0]
            heapq.heappush(pq, (sum_pair, nums1[i], nums2[0], 0))
        
        ans = []
        for _ in range(min(k, len(pq))):
            ele = heapq.heappop(pq)
            ans.append([ele[1], ele[2]])
            index_in_nums2 = ele[3]
            if index_in_nums2 + 1 < n2:
                new_sum = ele[1] + nums2[index_in_nums2 + 1]
                heapq.heappush(pq, (new_sum, ele[1], nums2[index_in_nums2 + 1], index_in_nums2 + 1))
        
        return ans