class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1

        curr_min = nums[0]
        for num in nums[1:]:
            if num - curr_min > k:
                ans += 1
                curr_min = num

        return ans