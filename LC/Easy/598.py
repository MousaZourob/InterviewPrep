class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0: return m*n
        min_row = inf
        min_col = inf
        
        for r, c in ops:
            min_row = min(r, min_row)
            min_col = min(c, min_col)
        
        return min_row * min_col
