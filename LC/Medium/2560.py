class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(guess):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= guess:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            
            return count == k

        l = min(nums)
        r = max(nums)
        ans = 0
        while l <= r:
            m = (r - l) // 2 + l
            print(l,r,m)

            if is_valid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans