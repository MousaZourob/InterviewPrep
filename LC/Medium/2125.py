class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_count = 0
        
        for row in bank:
            row_count = row.count('1')
            
            if row_count > 0:
                ans += prev_count * row_count
                prev_count = row_count
        
        return ans