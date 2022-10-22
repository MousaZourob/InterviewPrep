class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if not t or not s:
            return ""
        
        window_start = 0
        
        count = defaultdict(int)
        count_t = Counter(t)
        
        ans = float("inf"), None, None
        formed_ans = 0
        
        for window_end in range(len(s)):
            count[s[window_end]] += 1
            
            if s[window_end] in count_t and count[s[window_end]] == count_t[s[window_end]]:
                formed_ans += 1
            
            while formed_ans == len(count_t):
                if window_end - window_start + 1 < ans[0]:
                    ans = (window_end - window_start + 1, window_start, window_end)
                
                count[s[window_start]] -= 1
                
                if s[window_start] in count_t and count[s[window_start]] < count_t[s[window_start]]:
                    formed_ans -= 1
                window_start += 1
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]