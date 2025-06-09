class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        covered, ans, i= 0, 0, 0
        
        while covered < n:
            num = nums[i] if i < len(nums) else math.inf
            
            if num>covered+1:
                covered = covered*2 + 1
                ans += 1
            else:
                covered += num
                i += 1       
        
        return ans