class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        heap = []

        for char, count in freq.items():
            heappush(heap, (-count, char))
        
        ans = ""
        
        while heap:
            count, char = heappop(heap)
            ans += -1*count*char
        
        return ans