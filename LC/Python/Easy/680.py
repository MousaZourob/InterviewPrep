class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        
        while l <= r:
            if s[l] != s[r]:
                skip_l, skip_r = s[l+1:r+1], s[l:r]
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            else:
                r -= 1
                l += 1
        
        return True