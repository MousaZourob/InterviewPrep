class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        def count_pairs(guess):
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

        l = 0
        r = nums[-1] - nums[0]
        while l <= r:
            m = l + (r - l) // 2

            if count_pairs(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans