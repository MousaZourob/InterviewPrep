class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        l = 0
       
        p_count = [0]*26
        s_count = [0]*26
        
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        
        for r in range(len(s)):
            s_count[ord(s[r]) - ord('a')] += 1
            
            if r >= len(p):
                s_count[ord(s[l]) - ord('a')] -= 1
                l += 1
                
            if s_count == p_count:
                ans.append(l)
        
        return ans