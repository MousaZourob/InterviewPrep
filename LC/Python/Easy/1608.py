class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        freq = [0] * (n+1)
        for num in nums:
            freq[min(num,n)] += 1
        
        pre_sum = 0
        for x in range(n, 0, -1):
            pre_sum += freq[x]
            if pre_sum == x:
                return x
            
        return -1