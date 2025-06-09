class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        
        r_min_max = -inf
        for i in range(n):
            r_min = min(matrix[i])  
            r_min_max = max(r_min_max, r_min)

        c_max_min = inf
        for i in range(m):
            c_max = max(matrix[j][i] for j in range(n))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []