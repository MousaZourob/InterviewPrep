class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        heap = [-h for h in happiness]
        heapify(heap)
        
        for i in range(k):
            ans += max(-heappop(heap) - i, 0)
        
        return ans