class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)
        
        for row in matrix:
            if row[0]:
                row = [0 if r == 1 else 1 for r in row]
            count[tuple(row)] += 1
        
        return max(count.values())