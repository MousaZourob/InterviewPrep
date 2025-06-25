class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = []
        window_end = 0

        for i in range(n):
            if nums[i] == key:
                window_start = max(window_end, i - k)
                window_end = min(n-1, i + k) + 1
                ans.extend(range(window_start, window_end))

        return ans
