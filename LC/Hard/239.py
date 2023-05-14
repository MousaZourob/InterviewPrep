class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = []
        window_start = 0
        
        for window_end, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(window_end)
            
            if window_start > q[0]:
                q.pop(0)
            
            if window_end + 1 >= k:
                ans.append(nums[q[0]])
                window_start += 1
                
        return ans