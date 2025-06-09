class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        max_reachable = 0
        ans = 0
        
        while r < n - 1:
            max_reachable = max(max_reachable, l + nums[l])
            if l == r:
                r = max_reachable
                ans += 1
            l += 1
            
        return ans