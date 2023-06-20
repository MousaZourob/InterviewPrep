class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        window = sum(nums[:k+k])
        
        for i in range(k+k, n):
            window += nums[i]
            ans[i-k] = window//(k*2+1)
            window -= nums[i-k*2]
                    
        return ans