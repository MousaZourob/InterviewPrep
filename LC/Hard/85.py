class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRect(heights):
            stack = []
            res = 0

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    curr = stack.pop()
                    res = max(res, curr[1] * (i - curr[0]))
                    start = curr[0]

                stack.append((start,h))

            for i, h in stack:
                res = max(res, h * (len(heights)-i))

            return res
        
        ans = 0
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [0] * m
        
        for i in range(n):
            for j in range(m):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            ans = max(ans, largestRect(dp))
        
        return ans