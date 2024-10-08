class Solution:
    def minSwaps(self, s: str) -> int:
        count, swaps = 0, 0
        
        for c in s:
            if c == ']':
                count += 1
            else:
                count -= 1
            swaps = max(swaps, count)
            
        return ceil(swaps/2)