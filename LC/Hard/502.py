class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        heapq.heapify(max_heap)
        min_heap = []
        heapq.heapify(min_heap)
        
        for i, c in enumerate(capital):
            heapq.heappush(min_heap, (c, i))
        
        for _ in range(k):
            while min_heap and min_heap[0][0] <= w:
                cap, index = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-profits[index], index))
        
            
            if not max_heap:
                break
            
            w += -heapq.heappop(max_heap)[0]
            
        return w