class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        
        for n in gifts:
            heappush(heap, -n)
        
        while heap and k > 0:
            curr = heappop(heap)*-1
            
            curr = floor(sqrt(curr))
            
            if curr > 0:
                heappush(heap, -curr)
            
            k -= 1
            
        return -sum(heap)