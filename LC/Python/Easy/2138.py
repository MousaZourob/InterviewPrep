class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(0, n, k):
            if i + k > n:
                ans.append(s[i:] + fill*(i + k - n))
            else:
                ans.append(s[i:i+k])

        return ans