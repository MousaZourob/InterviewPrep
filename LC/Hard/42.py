class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        
        max_left = height[0]
        max_right = height[-1]
        
        l = 0
        r = n - 1
        
        while l < r:
            if height[l] <= height[r]:
                l += 1
                max_left = max(max_left, height[l])
                ans += max_left - height[l]        
            else:
                r -= 1
                max_right = max(max_right, height[r])
                ans += max_right - height[r]
        
        return ans