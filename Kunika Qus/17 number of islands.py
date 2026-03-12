'''Given a grid of size N x M (N is the number of rows and M is the number of columns in the grid) consisting of '0's (Water) and ‘1's(Land). Find the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.
'''
'''input: grid = [ ["1", "1", "1", "0", "1"], ["1", "0", "0", "0", "0"], ["1", "1", "1", "0", "1"], ["0", "0", "0", "1", "1"] ]

Output: 2

Explanation: This grid contains 2 islands. Each '1' represents a piece of land, and the islands are formed by connecting adjacent lands horizontally or vertically. Despite some islands having a common edge, they are considered separate islands because there is no land connectivity in any of the eight directions between them. Therefore, the grid contains 2 islands.

Input: grid = [ ["1", "0", "0", "0", "1"], ["0", "1", "0", "1", "0"], ["0", "0", "1", "0", "0"], ["0", "1", "0", "1"," 0"] ]

Output: 1

Explanation: In the given grid, there's only one island as all the '1's are connected either horizontally, vertically, or diagonally, forming a single contiguous landmass surrounded by water on all sides.

'''

class Solution:
    # Time Complexity: O(N * M) + O(N*M*9) for the BFS traversal
    # Space Complexity: O(N * M) + O(N * M ) for queue and for the visited matrix
    # where N is the number of rows and M is the number of columns in the grid.
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        vis = [[False]*m for _ in range(n)]

        c = 0
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col] == '1':
                    c += 1
                    self.bfs(row, col, vis, grid)
        return c

    def bfs(self, row, col, vis, grid):
        from collections import deque
        q = deque()
        q.append([row, col])
        vis[row][col] = True
        n = len(grid)
        m = len(grid[0])
        while q:
            nrow, ncol = q.popleft()   # for 4 directions, we can use dr = [-1, 0, 1, 0] and dc = [0, 1, 0, -1] and for i in range(4) and newrow = nrow + dr[i] and newcol = ncol + dc[i]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    newrow = nrow + i
                    newcol = ncol + j
                    

                    if newrow >= 0 and newrow < n and newcol >= 0 and newcol < m and grid[newrow][newcol] == '1' and vis[newrow][newcol] == False:
                        q.append([newrow, newcol])
                        vis[newrow][newcol] = True



       