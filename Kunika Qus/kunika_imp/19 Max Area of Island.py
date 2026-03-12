'''
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''


class Solution:
    # DFS Approach
    # Time Complexity: O(m*n) for traversing the entire grid once  + O(4*m*n) for DFS calls in worst case
    # Space Complexity: O(m*n) for visited array and recursion stack
    def dfs(self, r, c, vis, grid, dr, dc):
        vis[r][c] = True
        count = 1
        for i in range(4):
            newr = dr[i]+r
            newc = dc[i] +c

            if newr >=  0 and newr < len(grid) and newc >=0 and newc <len(grid[0]) and grid[newr][newc] == 1 and vis[newr][newc] == False:
                count += self.dfs(newr, newc, vis, grid, dr, dc)
                
        return count


    # BFS Approach
    # Time Complexity: O(m*n) for traversing the entire grid once  + O(4*m*n) for BFS calls in worst case
    # Space Complexity: O(m*n) for visited array and queue space
    def bfs(self, i, j, dr, dc, grid, vis):
        import queue
        q = queue.Queue()
        q.put([i, j])
        vis[i][j] = True
        count = 0

        while not q.empty():
            r, c = q.get()
            count += 1
            for key in range(4):
                newr = dr[key]+ r 
                newc = dc[key] + c

                if newr >=  0 and newr < len(grid) and newc >=0 and newc <len(grid[0]) and grid[newr][newc] == 1 and vis[newr][newc] == False:
                    q.put([newr, newc])
                    vis[newr][newc] = True 

        return count



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid),len(grid[0])

        vis = [[False for _ in range(m)] for _ in range(n)]

        dr = [-1, 0, +1, 0]
        dc = [0, +1, 0, -1]
    
        maxi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    # maxi = max(maxi, self.dfs(i, j, vis, grid, dr, dc))
                    maxi = max(maxi, self.bfs(i, j, dr, dc, grid, vis))
                    print(maxi)

        return maxi
                    


        