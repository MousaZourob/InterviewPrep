class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_ctr = Counter(s)
        
        for i in range(len(s)):
            if s_ctr[s[i]] == 1:
                return i 
        
        return -1