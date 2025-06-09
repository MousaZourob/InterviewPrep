class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = [1] * len(obstacles)
        lis = []
        
        for i, height in enumerate(obstacles):
            idx = bisect_right(lis, height)
            
            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height
            ans[i] = idx + 1
        
        return ans