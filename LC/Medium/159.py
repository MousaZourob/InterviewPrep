class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = defaultdict(int)
        window_start = 0
        ans = 0
        
        for window_end in range(len(s)):
            count[s[window_end]] += 1
            
            while len(count) > 2:
                count[s[window_start]] -= 1
                if count[s[window_start]] == 0:
                    del count[s[window_start]]
                window_start += 1    
            
            ans = max(ans, window_end - window_start + 1)
        
        return ans