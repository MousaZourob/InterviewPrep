class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        heap = []
        
        for n, c in count.items():
            heappush(heap, (c, n))
        
        while heap and k > 0:
            c, n = heappop(heap)
            
            if k >= c:
                k -= c
            else:
                return len(heap) + 1
            
        return len(heap)
    