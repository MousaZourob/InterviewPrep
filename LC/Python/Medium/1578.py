class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        window_start = 0
        curr_total = 0
        curr_max = 0
        
        for window_end in range(len(colors)):
            if colors[window_start] == colors[window_end]:
                curr_total += neededTime[window_end]
                curr_max = max(curr_max, neededTime[window_end])
            else:
                ans += curr_total - curr_max
                window_start = window_end
                curr_total = neededTime[window_end]
                curr_max = neededTime[window_end]
                
        ans += curr_total - curr_max
        return ans