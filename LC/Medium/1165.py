class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        
        heapify(sticks)
        
        while len(sticks) > 1:
            n1, n2 = heappop(sticks), heappop(sticks)
            ans += n1 + n2
            heappush(sticks, n1 + n2)
        
        return ans