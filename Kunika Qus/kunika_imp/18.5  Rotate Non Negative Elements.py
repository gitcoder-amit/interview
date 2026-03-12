'''
3819. Rotate Non Negative Elements

You are given an integer array nums and an integer k.

Rotate only the non-negative elements of the array to the left by k positions, in a cyclic manner.

All negative elements must stay in their original positions and must not move.

After rotation, place the non-negative elements back into the array in the new order, filling only the positions that originally contained non-negative values and skipping all negative positions.

Return the resulting array.

 

Example 1:

Input: nums = [1,-2,3,-4], k = 3

Output: [3,-2,1,-4]

Explanation:​​​​​​​

The non-negative elements, in order, are [1, 3].
Left rotation with k = 3 results in:
[1, 3] -> [3, 1] -> [1, 3] -> [3, 1]
Placing them back into the non-negative indices results in [3, -2, 1, -4].
Example 2:

Input: nums = [-3,-2,7], k = 1

Output: [-3,-2,7]

Explanation:

The non-negative elements, in order, are [7].
Left rotation with k = 1 results in [7].
Placing them back into the non-negative indices results in [-3, -2, 7].
Example 3:

Input: nums = [5,4,-9,6], k = 2

Output: [6,5,-9,4]

Explanation:

The non-negative elements, in order, are [5, 4, 6].
Left rotation with k = 2 results in [6, 5, 4].
Placing them back into the non-negative indices results in [6, 5, -9, 4].
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
0 <= k <= 105

'''



class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n) for storing non-negative elements
    def reverse(self, arr, left, right):
        if len(arr) <= 1:
            return
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def left_rotate(self, arr, k):
        n = len(arr)
        if n == 0:
            return arr
        
        k = k % n  # handle k > n
        # return arr[k:] + arr[:k]
        self.reverse(arr, 0, k-1)
        self.reverse(arr, k, n-1)
        self.reverse(arr, 0, n-1)

            
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pos = []
        for num in nums:
            if num >= 0:
                pos.append(num)

        
        # self.reverse(pos, 0, k%len(pos)-1)
        # self.reverse(pos, k%len(pos), len(pos)-1)
        # self.reverse(pos, 0, len(pos)-1)
        self.left_rotate(pos, k)
        # print(pos)
        
        index = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] = pos[index]
                index += 1

        return nums