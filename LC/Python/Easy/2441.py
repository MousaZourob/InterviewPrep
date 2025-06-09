class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        found = set()
        ans = -1
        
        for num in nums:
            if num*-1 in found:
                ans = max(ans, abs(num))
            found.add(num)
            
        return ans