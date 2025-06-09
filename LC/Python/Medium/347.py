class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqs = [[] for _ in range(n)]
        count = Counter(nums)
        
        for key, v in count.items():
            freqs[v-1].append(key)
            
        ans = []
        for i in range(n-1,-1,-1):
            for n in freqs[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return ans