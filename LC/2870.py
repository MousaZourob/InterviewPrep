class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count  = Counter(nums)
        ans = 0
        
        for v in count.values():
            if v == 1:
                return -1
            ans += ceil(v / 3)
            
        return ans