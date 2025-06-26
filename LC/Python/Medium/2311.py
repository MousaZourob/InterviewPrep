class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        curr = 0
        bits = k.bit_length()

        for i, c in enumerate(s[::-1]):
            if c == '0':
                ans += 1
            else:
                if i < bits and curr + (1 << i) <= k:
                    curr += (1 << i)
                    ans += 1

        return ans