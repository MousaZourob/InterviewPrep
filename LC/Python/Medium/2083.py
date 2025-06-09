class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(int)
        ans = 0
        
        for c in s:
            count[c] += 1
            ans += count[c]
            
        return ans