class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        curr = []
        def dfs(i):
            if i >= len(nums):
                ans.append(list(curr))
                return
            
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)
        
        dfs(0)
        
        return ans