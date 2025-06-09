class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn = len(s)
        tn = len(t)
        
        if sn != tn: return False
        
        s_count = [0]*26
        t_count = [0]*26
        
        for i in range(sn):
            s_count[ord(s[i])-ord('a')] += 1
            t_count[ord(t[i])-ord('a')] += 1
            
        return s_count == t_count