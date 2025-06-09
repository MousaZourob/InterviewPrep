class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != "O":
                return
            board[r][c] = 'E'
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r+x, c+y)
        
        border = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i in [0, m-1] or j in [0, n-1]):
                    border.append((i, j))

        for i, j in border:
            dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"