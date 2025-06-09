class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        def find(l, r):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                    
            return -1
                    
        l = 0
        r = n - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[-1] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return max(find(0, l - 1), find(l, n - 1))