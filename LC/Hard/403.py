class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        goal = stones[-1]
        stones = set(stones)
        
        def dfs(stone, k):
            if stone == goal:
                return True
            if (stone, k) in dp:
                return dp[(stone, k)]
            
            res = False
            for nk in range(k-1, k+2):
                if nk > 0 and stone + nk in stones:
                    res |= dfs(stone + nk, nk)
            
            dp[(stone, k)] = res
            return res
        
        return dfs(0, 0)