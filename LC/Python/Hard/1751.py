class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        dp = {}
        n = len(events)
        events.sort()
        
        def dfs(i, attended):
            if attended <= 0:
                return 0
            if i >= n:
                return 0
            if (i,attended) in dp:
                return dp[(i,attended)]
            
            curr_event = events[i]
            next_event = bisect.bisect_left(events, [curr_event[1] + 1])
            
            dp[(i,attended)] = max(curr_event[2] + dfs(next_event, attended - 1), dfs(i+1, attended))
            
            return dp[(i,attended)]
        
        return dfs(0, k)