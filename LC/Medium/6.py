class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        ans = [[] for _ in range(numRows)]
        row_idx = 0
        going_up = True

        for ch in s:
            ans[row_idx].append(ch)
            if row_idx == numRows - 1:
                going_up = False
            elif row_idx == 0:
                going_up = True
            
            if going_up:
                row_idx += 1
            else:
                row_idx -= 1
                
        return "".join(["".join(row) for row in ans])