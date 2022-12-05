class Solution:
    def numDecodings(self, s: str) -> int:
        dp = 0
        dp1 = 1
        dp2 = 0
        
        for i in range(len(s)-1,-1,-1):
            if s[i] != '0':
                dp += dp1

                if i + 1 < len(s) and int(s[i:i+2]) < 27:
                    dp += dp2
            
            dp2 = dp1
            dp1 = dp
            dp = 0
        
        return dp1