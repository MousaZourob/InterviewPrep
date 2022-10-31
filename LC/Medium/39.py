class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(i, curr, total):
            if total == target:
                ans.append(list(curr))
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            
            curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        
        return ans