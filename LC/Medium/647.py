class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(start, left, right):
            pal = 0
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                pal += 1
            return pal

        ans = 0
        
        for i in range(len(s)):
            ans += expand(i, i, i)
            ans += expand(i, i, i+1)
                
        return ans