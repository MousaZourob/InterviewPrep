class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                   
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])
                
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])
                
                idx = (r // 3) * 3 + c // 3
                if board[r][c] in boxs[idx]:
                    return False
                boxs[idx].add(board[r][c])
                
        return True