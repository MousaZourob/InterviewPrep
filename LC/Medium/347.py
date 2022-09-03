class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        
        for num, freq in freq.items():
            heappush(heap, (freq, num))
            
            if len(heap) > k:
                heappop(heap)
        
        return [row[1] for row in heap]