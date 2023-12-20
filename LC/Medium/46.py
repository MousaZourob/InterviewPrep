class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        curr = []        
        def dfs(i):
            if i >= n:
                ans.append(list(curr))
                return 
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(i+1)
                    curr.pop()                 
        
        dfs(0)
        return ans