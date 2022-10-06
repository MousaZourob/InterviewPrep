class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = inf, inf
        
        for k in nums:
            if k <= i:
                i = k
            elif k <= j:
                j = k
            else:
                return True
        return False