class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for n in arr:
            heappush(heap, (abs(n-x), n))
            
        ans = []
        for _ in range(k): 
            ans.append(heappop(heap)[1])
                
        return sorted(ans)