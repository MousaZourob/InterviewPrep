class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        ans = 0
        window_start = 0
        
        for window_end in range(len(s)):
            seen[s[window_end]] += 1
            
            if window_end - window_start + 1 - max(seen.values()) > k:
                seen[s[window_start]] -= 1
                window_start += 1
            
            ans = max(ans, window_end - window_start + 1)
        
        return ans