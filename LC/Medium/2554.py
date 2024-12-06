class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0
        
        for num in range(1, n + 1):
            if num in banned:
                continue
            
            if maxSum - num < 0:
                return ans
            
            maxSum -= num
            ans += 1
        
        return ans