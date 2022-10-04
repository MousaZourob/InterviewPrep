class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        window_start = 0
        
        for window_end in range(1, len(colors)):
            if colors[window_start] == colors[window_end]:
                total_time += min(neededTime[window_start], neededTime[window_end])
                
                if neededTime[window_start] < neededTime[window_end]:
                    window_start = window_end
            else:
                window_start = window_end
            
        return total_time