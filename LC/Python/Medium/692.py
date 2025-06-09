class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        
        for word, count in freq.items():
            heappush(heap, (-count, word))
        
        ans = []
        while k > 0:
            ans.append(heappop(heap)[1])
            k -= 1
            
        return ans