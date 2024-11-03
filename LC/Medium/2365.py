class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        ans = 0
        cooldowns = {}
        for task in tasks:
            if task not in cooldowns:
                cooldowns[task] = -inf
            ans = max(ans, cooldowns[task] + space) + 1
            cooldowns[task] = ans
            
        return ans