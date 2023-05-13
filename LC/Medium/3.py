class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        window_start = 0
        
        for window_end in range(len(s)):
            while s[window_end] in seen:
                seen.remove(s[window_start])
                window_start += 1
            
            seen.add(s[window_end])
            ans = max(ans, window_end - window_start + 1)
        
        return ans
        