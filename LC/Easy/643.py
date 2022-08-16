class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        ans = curr_sum
        
        for l in range(1, len(nums)-k+1):
            curr_sum -= nums[l-1]
            curr_sum += nums[l+k-1]
            ans = max(ans, curr_sum)
        
        return ans/k