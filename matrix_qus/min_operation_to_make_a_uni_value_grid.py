'''
2033. Minimum Operations to Make a Uni-Value Grid
Medium

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.


Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

'''

# for any doubt read leetcode editorial
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_array = []
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                nums_array.append(grid[i][j])

        nums_array.sort()

        median = len(nums_array)//2

        for num in nums_array:
            if num%x != nums_array[median]%x:
                return -1
            
            result += abs(nums_array[median]-num)//x
        return result
        
        