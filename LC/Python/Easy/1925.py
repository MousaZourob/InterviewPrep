class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0

        for i in range(1, n+1):
            for j in range (1, n+1):
                res = sqrt(i * i + j * j)
                if res.is_integer() and res <= n:
                    ans += 1

        return ans
