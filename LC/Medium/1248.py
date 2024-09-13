class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        odd_count = 0
        l, m = 0, 0
        
        for r in range(len(nums)):
            if nums[r] % 2:
                odd_count += 1
            
            while odd_count > k:
                if nums[l] % 2:
                    odd_count -= 1
                
                l += 1
                m = l
            
            if odd_count == k:
                while not nums[m] % 2:
                    m += 1
                ans += (m - l) + 1  
                    
        return ans   