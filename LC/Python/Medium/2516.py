class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = [0] * 3
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for c in count:
            if c < k:
                return -1

        window_start = 0
        ans = 0

        for window_end in range(len(s)):
            count[ord(s[window_end]) - ord('a')] -= 1
    
            while count[0] < k or count[1] < k or count[2] < k:
                count[ord(s[window_start]) - ord('a')] += 1
                window_start += 1

            ans = max(ans, window_end - window_start + 1)

        return n - ans