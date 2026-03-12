'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution:
    # DFS Approach
    # Time Complexity: O(m*n) for traversing the entire grid once  + O(4*m*n) for DFS calls in worst case
    # Space Complexity: O(m*n) for visited array and recursion stack
    def dfs(self,row,col,vis, grid, dr, dc):
        vis[row][col] = True
        for i in range(4):
            newr = dr[i]+row
            newc = dc[i]+col

            if newr >= 0 and newr < len(grid) and newc >= 0 and newc < len(grid[0]) and grid[newr][newc] == '1' and not vis[newr][newc]:
                self.dfs(newr, newc, vis, grid, dr,dc)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        dr = [-1, 0, +1, 0]
        dc = [0, +1, 0, -1]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not vis[r][c]:
                    self.dfs(r, c, vis, grid, dr, dc) # or bfs
                    count += 1
        return count
        