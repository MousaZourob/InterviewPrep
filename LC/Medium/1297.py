class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        sub_counts = defaultdict(int)
        char_count = defaultdict(int)
        window_start = 0
        
        for window_end in range(n):
            word = s[window_start: window_end+1]
            char_count[s[window_end]] += 1
            if window_end - window_start + 1 == minSize and len(char_count) <= maxLetters:
                sub_counts[word] += 1
            
            if window_end - window_start + 1 >= minSize:
                char_count[s[window_start]] -= 1
                if char_count[s[window_start]] == 0:
                    del char_count[s[window_start]]
                window_start += 1
        
        return max(sub_counts.values()) if sub_counts else 0
