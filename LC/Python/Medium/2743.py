class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        seen = [0]*26
        ans = 0
        window_start = 0
        
        for window_end in range(len(s)):
            seen[ord(s[window_end]) - ord('a')] += 1

            while seen[ord(s[window_end]) - ord('a')] > 1:
                seen[ord(s[window_start]) - ord('a')] -= 1
                window_start += 1
    
            ans += window_end - window_start + 1
            
        return ans