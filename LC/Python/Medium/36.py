class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = int(board[r][c]) - 1

                if rows[r][num] == 1:
                    return False
                rows[r][num] = 1

                if cols[c][num] == 1:
                    return False
                cols[c][num] = 1

                box = (r//3) * 3 + (c//3)
                if boxes[box][num] == 1:
                    return False
                boxes[box][num] = 1

        return True