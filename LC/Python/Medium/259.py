class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        for i, num in enumerate(nums[:-2]):
            l = i + 1
            r = n - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if curr < target:
                    ans += r - l
                    l += 1
                else:
                    r -= 1
                    
        return ans
