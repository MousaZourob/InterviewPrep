class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        neg_count = 0
        smallest_neg = inf
    
        for row in matrix:
            for num in row:
                ans += abs(num)
                smallest_neg = min(abs(smallest_neg), abs(num))
                if num < 0:
                    neg_count += 1
                
        if neg_count % 2 == 1: ans -= smallest_neg*2
        return ans