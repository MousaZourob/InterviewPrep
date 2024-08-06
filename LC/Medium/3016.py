class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        
        ans = 0
        i = 0
        
        while heap:
            ans += (1 + i // 8) * -heappop(heap)
            i += 1
            
        return ans