class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0
        total = sum(nums)
        curr = 0

        for num in nums:
            curr += num
            total -= num

            if num != 0:
                continue

            if curr == total:
                ans += 2
            elif abs(curr - total) == 1:
                ans += 1

        return ans