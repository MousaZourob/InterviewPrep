class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                num = nums[r]
                r -= 1
            else:
                num = nums[l]
                l += 1
            
            ans[i] = num * num
        return ans