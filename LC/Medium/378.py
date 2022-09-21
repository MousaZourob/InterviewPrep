class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for row in matrix:
            for num in row:
                heappush(heap, -num)
                
                if len(heap) > k:
                    heappop(heap)
                    
        return -heap[0]