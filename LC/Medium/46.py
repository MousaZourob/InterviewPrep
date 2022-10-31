class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [list(nums)]
        
        ans = []
        
        def dfs(first):
            if first == n:
                ans.append(list(nums))
            
            for i in range(first, n):
                nums[first], nums[i]  = nums[i], nums[first]
                dfs(first+1)
                nums[first], nums[i]  = nums[i], nums[first]
            
        
        dfs(0)
        return ans