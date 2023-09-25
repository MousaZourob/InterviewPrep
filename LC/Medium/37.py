class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
                
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        ans = [False]
        
        def backtrack(i, j):
            if i == 9:
                ans[0] = True
                return
            
            new_i = i + (j + 1)//9
            new_j = (j + 1) % 9
            
            if board[i][j] != '.':
                backtrack(new_i, new_j)
            else:
                for guess in range(1, 10):
                    box_num = (i//3) * 3 + (j//3)
                    
                    if guess not in rows[i] and guess not in cols[j] and guess not in boxs[box_num]:
                        rows[i].add(guess)
                        cols[j].add(guess)    
                        boxs[box_num].add(guess)
                        board[i][j] = str(guess)
                        
                        backtrack(new_i, new_j)
                        
                        if not ans[0]:
                            rows[i].remove(guess)
                            cols[j].remove(guess)    
                            boxs[box_num].remove(guess)
                            board[i][j] = '.'
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c])
                    rows[r].add(val)
                    cols[c].add(val)
                    
                    box_num = (r//3) * 3 + (c//3)
                    boxs[box_num].add(val)
        
        backtrack(0, 0)