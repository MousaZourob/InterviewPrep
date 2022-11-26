class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        n = len(profit)
        startTime = [jobs[i][0] for i in range(n)]
        dp = {}
        
        def dfs(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            
            j = bisect_left(startTime, jobs[i][1])
            dp[i] = max(jobs[i][2] + dfs(j), dfs(i+1))
            
            return dp[i]
            
        return dfs(0)