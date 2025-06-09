class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxs = [[0] * 9 for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c]) - 1

                    if rows[r][val] == 1:
                        return False
                    rows[r][val] = 1

                    if cols[c][val] == 1:
                        return False
                    cols[c][val] = 1
                    
                    box_num = (r//3) * 3 + (c//3)
                    if boxs[box_num][val] == 1:
                        return False
                    boxs[box_num][val] = 1
        
        return True