class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        dp = [0] * n
        start_times = [job[0] for job in jobs]
        
        def dfs(i):
            if i >= n:
                return 0
            if dp[i]:
                return dp[i]
            
            j = bisect_left(start_times, jobs[i][1])
                        
            dp[i] = max(jobs[i][2] + dfs(j), dfs(i+1))
            return dp[i]
        
        return dfs(0)