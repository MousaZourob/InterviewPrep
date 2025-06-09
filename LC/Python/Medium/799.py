class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]
        
        for r in range(1, query_row + 1):
            curr_row = [0] *(r + 1)
            for i in range(r):
                extra = prev_row[i] - 1
                if extra > 0:
                    curr_row[i] += extra / 2
                    curr_row[i + 1] += extra / 2
            prev_row = curr_row

        return min(1, prev_row[query_glass])