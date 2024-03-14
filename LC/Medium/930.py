class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        
        window_start = 0
        pre_zeros = 0
        curr_sum = 0
        
        for window_end in range(len(nums)):
            curr_sum += nums[window_end]
            
            while window_start < window_end and (nums[window_start] == 0 or curr_sum > goal):
                if nums[window_start] == 1:
                    pre_zeros = 0
                else:
                    pre_zeros += 1
                    
                curr_sum -= nums[window_start]
                window_start += 1
            
            if curr_sum == goal:
                ans += 1 + pre_zeros
        
        return ans