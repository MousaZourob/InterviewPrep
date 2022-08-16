class Solution:
    def romanToInt(self, s: str) -> int:
        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and rti[s[i]] < rti[s[i+1]]:
                ans -= rti[s[i]]
            else:
                ans += rti[s[i]]
        
        return ans