class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        
        heap = []
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
            
        ans = 0
        while heap:
            num, i = heappop(heap)
            if not marked[i]:
                ans += num
                
                marked[i] = True
                
                if i - 1 >= 0:
                    marked[i - 1] = True
                if i + 1 < n:
                    marked[i + 1] = True
        
        return ans