class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pos = {}
        ans = -1
        
        for i,c in enumerate(s):
            if c not in pos:
                pos[c] = i
            else:
                ans = max(ans, i - pos[c] - 1)
                
        return ans