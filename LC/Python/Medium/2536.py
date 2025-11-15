class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        diff = [[0] * (n+1) for _ in range(n+1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] +=1
        
        for i in range(n):
            for j in range(n):
                ans[i][j] = diff[i][j]
                if i > 0:
                    ans[i][j] += ans[i-1][j]
                if j > 0:
                    ans[i][j] += ans[i][j-1]
                if i > 0 and j > 0:
                    ans[i][j] -= ans[i-1][j-1]

        return ans