class Solution:
    def printboard(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j])
            print()

    # Time Complexity: O(n!) due to the recursive nature of the solution
    # Space Complexity: O(n^2)
    def helper(self, board, col, ans):
        if col == len(board):
            ans.append([''.join(row) for row in board])
            return

        for row in range(len(board)):
            if self.is_safe(board, row, col):
                board[row][col] = 'Q'
                self.helper(board, col+1, ans)
                board[row][col] = '.'

    def is_safe(self, board, row, col):
        for c in range(col, -1, -1):
            if board[row][c] == 'Q':
                return False
        
        r, c = row, col
        while c >= 0 and r < len(board):
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1
        
        r,c = row, col
        while c >= 0 and r >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        
        return True

    

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for i in range(n)]
        ans = []
        self.helper(board, 0, ans)
        return ans
        
        