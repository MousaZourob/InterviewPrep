class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        buckets = [[] for _ in range(max(freq.values())+1)]
        
        for c, i in freq.items():
            buckets[i].append(c)
            
        ans = []
        for i in range(len(buckets) -1, 0, -1):
            for c in buckets[i]:
                ans.append(c*i)
        
        return "".join(ans)