'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
'''


class Solution:
    # Time Complexity: O(n*m*8) where n is number of rows and m is number of columns
    # Space Complexity: O(n*m) for visited array
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]

        for r in range(n):
            for c in range(m):
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        newRow = r + i
                        newCol = c + j
                        
                        if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m and board[newRow][newCol] == 1:
                            count += 1
                
                if (count < 2 or count > 3) and board[r][c] == 1:
                    vis[r][c] = 0
                elif board[r][c] == 0 and count == 3:
                    vis[r][c] = 1
                else:
                    vis[r][c] = board[r][c]
        
        for i in range(n):
            for j in range(m):
                board[i][j] = vis[i][j]

    # Better Approach:
    # Time Complexity: O(n*m*8) where n is number of rows and m
    # Space Complexity: O(1)
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        for r in range(n):
            for c in range(m):
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        newRow = r + i
                        newCol = c + j
                        
                        if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m and abs(board[newRow][newCol]) == 1:
                            count += 1
                
                if (count < 2 or count > 3) and board[r][c] == 1:
                    board[r][c] = -1  # Live to dead
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2   # Dead to live
        
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
