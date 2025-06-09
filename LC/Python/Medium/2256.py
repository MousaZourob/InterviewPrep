class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        past_sum = 0
        past_len = 0
        post_sum = sum(nums)
        post_len = len(nums)

        ans = [inf, inf]
        
        for i in range(len(nums)):
            past_sum += nums[i]
            past_len += 1
            post_sum -= nums[i]
            post_len -= 1
    
            if post_len == 0:
                curr = abs(past_sum//past_len)
            else:
                curr = abs(past_sum//past_len - post_sum//post_len)
                
            if ans[0] > curr:
                ans = [curr, i]
                
        return ans[1]