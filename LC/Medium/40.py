class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        
        subset = []
        def dfs(i, total):
            if total == target:
                ans.append(list(subset))
                
            if total > target or i >= n:
                return
            
            prev = -1
            for i in range(i, n):
                if candidates[i] == prev:
                    continue
                subset.append(candidates[i])
                dfs(i+1, total+candidates[i])
                subset.pop()
                prev = candidates[i]
        
        dfs(0,0)
        
        return ans