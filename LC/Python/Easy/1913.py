class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = -1
        max2 = -1
        min1 = inf
        min2 = inf
        
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            else:
                max2 = max(max2, num)
                
            if num < min1:
                min2 = min1
                min1 = num
            else:
                min2 = min(min2, num)
                
        return max1*max2 - min1*min2