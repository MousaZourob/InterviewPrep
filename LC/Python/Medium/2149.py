class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        neg = 1
        pos = 0
        
        for num in nums:
            if num > 0:
                ans[pos] = num
                pos += 2
            else:
                ans[neg] = num
                neg += 2
            
        return ans