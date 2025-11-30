class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        ans = n
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0

        mods = {}
        mods[0] = -1

        curr = 0
        for i in range(n):
            curr = (curr + nums[i]) % p
            needed = (curr - target + p) % p

            if needed in mods:
                ans = min(ans, i - mods[needed])
            
            mods[curr] = i
            
        return ans if ans != n else -1
