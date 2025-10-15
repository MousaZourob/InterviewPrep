class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev = 0
        curr = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            
            if (prev >= k and curr >= k) or (curr >= 2 * k):
                return True

        return False
