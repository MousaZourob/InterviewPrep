class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        ans = 0
        
        for c in s:
            if c== '(':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    ans += 1
        
        return ans + count