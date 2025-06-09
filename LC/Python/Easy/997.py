class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1

        in_degrees = [0] * (n + 1)

        for a, b in trust:
            in_degrees[a] -= 1
            in_degrees[b] += 1

        for i, score in enumerate(in_degrees[1:], 1):
            if score == n - 1:
                return i
        return -1