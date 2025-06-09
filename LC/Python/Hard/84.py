class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                curr = stack.pop()
                ans = max(ans, curr[1] * (i - curr[0]))
                start = curr[0]
            
            stack.append((start,h))
        
        for i, h in stack:
            ans = max(ans, h * (len(heights)-i))
        
        return ans