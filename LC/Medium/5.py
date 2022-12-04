class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
            
        ans_l, ans_r = 0, 0
        
        for i in range(len(s)):
            curr = max(expand(i, i), expand(i, i+1))
            
            if curr > ans_r - ans_l:
                ans_l = i - (curr - 1) // 2
                ans_r = i + curr // 2
                
        return s[ans_l:ans_r+1]
    
    