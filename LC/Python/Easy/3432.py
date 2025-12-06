class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0

        l = 0
        r = sum(nums)

        for i in range(1, len(nums)-1):
            if (l - r) % 2 == 0:
                ans += 1
            l += nums[i]
            r -= nums[i]
        
        if (l - r) % 2 == 0:
            ans += 1

        return ans
