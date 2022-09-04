class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = []
        
        for num, count in freq.items():
            heappush(heap, (count, num))
        
        while heap and k:
            count, num = heappop(heap)
            
            if k >= count:
                k -= count
            else:
                return len(heap) + 1
        
        return len(heap)