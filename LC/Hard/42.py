class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        max_left = 0
        r = len(height) - 1
        max_right = 0
        ans = 0
         
        while l <= r:
            if max_left <= max_right:
                if min(max_left, max_right) - height[l] > 0:    
                    ans += min(max_left, max_right) - height[l]
                max_left = max(max_left, height[l])
                l += 1
            else:
                i = r
                if min(max_left, max_right) - height[r] > 0:    
                    ans += min(max_left, max_right) - height[r]
                max_right = max(max_right, height[r])
                r -= 1
            
        return ans