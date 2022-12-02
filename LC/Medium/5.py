class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(start, left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return right - left - 1

        ans_l, ans_r = 0, 0
        
        for i in range(len(s)):
            ans = max(expand(ans_l, i, i), expand(ans_l, i, i+1))
            
            if ans > ans_r - ans_l:
                ans_l = i - (ans-1) // 2
                ans_r = i + ans // 2
                
        return s[ans_l:ans_r+1]
    