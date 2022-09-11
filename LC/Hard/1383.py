class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        curr_sum = 0
        ans = -inf
        
        for e, s in sorted(zip(efficiency, speed),reverse=True):
            heappush(heap, s)
            curr_sum += s
            ans = max(ans, curr_sum*e)

            while len(heap) >= k:
                curr_sum -= heappop(heap)
        
        return ans % (10**9+7)