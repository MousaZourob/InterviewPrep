class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            min_s = ""
            for i in range(len(s)):
                if i == 0:
                    min_s = s[i:] + s[:i]
                else:
                    min_s = min(min_s, s[i:] + s[:i])
            return min_s
        else:
            return "".join(sorted(s))