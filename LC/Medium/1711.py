class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for food in deliciousness:
            for i in range(22):
                ans += freq[2**i - food]
            freq[food] += 1
        
        return ans % (10**9+7)