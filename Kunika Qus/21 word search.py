# 79. Word Search

'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

'''



class Solution:
    # Time Complexity: O(N * M * 4^(L)) where N is the number of rows, M is the number of columns, and L is the length of the word.
    def dfs(self, row, col, vis, board, word, index, dr, dc, n, m):
        vis[row][col] = True
        # s += board[row][col]

        if board[row][col] != word[index]:
            return False

        if index == len(word) - 1:
            return True


        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < m and not vis[nr][nc]:
                if self.dfs(nr, nc, vis, board, word, index+1, dr,dc, n, m):
                    return True
                else:
                    vis[nr][nc] = False
        vis[row][col] = False
        # s = s[:-1]
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        vis = [[False] * m for _ in range(n)]
        dr = [0, -1, 0, +1]
        dc = [-1, 0, +1, 0]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, vis, board, word, 0, dr, dc, n, m):
                        return True
        return False



    # in this less test case passed due to the string concatenation in the dfs function and in python string concatenation is costly

     def dfs(self, row, col, vis, board, word, index, dr, dc, n, m):
        vis[row][col] = True
        s += board[row][col]

        if s == word:
            return True

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < m and not vis[nr][nc]:
                if self.dfs(nr, nc, vis, board, word, s, dr,dc, n, m):
                    return True
                else:
                    vis[nr][nc] = False
        vis[row][col] = False
        s = s[:-1]
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        vis = [[False] * m for _ in range(n)]
        dr = [0, -1, 0, +1]
        dc = [-1, 0, +1, 0]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, vis, board, word, "", dr, dc, n, m):
                        return True
        return False
        