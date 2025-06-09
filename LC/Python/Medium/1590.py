class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p
        n = len(nums)
        
        if rem == 0:
            return 0
        
        ans = len(nums)
        curr_sum = 0
        rem_idx = {
            0: -1
        }
        
        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            pre = (curr_sum - rem + p) % p
            if pre in rem_idx:
                ans = min(ans, i - rem_idx[pre])
            rem_idx[curr_sum] = i
        
        return -1 if ans == n else ans