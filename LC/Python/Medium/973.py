class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)

        for point in points:
            heappush(heap, (-sqrt(point[0]**2 + point[1]**2), point))
            if len(heap) > k:
                heappop(heap)

        ans = [row[1] for row in heap]
        
        return ans