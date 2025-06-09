class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        subset = []
        def dfs(i, total):
            if total == target:
                ans.append(list(subset))
                return
            if i >= len(candidates) or total > target:
                return
            
            subset.append(candidates[i])
            dfs(i, total + candidates[i])
            
            subset.pop()
            dfs(i+1, total)
            
        dfs(0, 0)
        
        return ans