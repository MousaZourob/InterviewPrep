class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        
        def countPairs(guess):
            i, c = 0, 0
                        
            while i < n - 1:
                if nums[i + 1] - nums[i] <= guess:
                    i += 2
                    c += 1
                else:
                    i += 1
                
                if c >= p:
                    return True
            
            return False
        
        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            m = l + (r-l) // 2
            
            if countPairs(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans