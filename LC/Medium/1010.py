class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = defaultdict(int)
        
        ans = 0
        for dur in time:
            if dur % 60 == 0:
                ans += freq[dur % 60]
            else:
                ans += freq[60 - dur % 60]
            freq[dur % 60] += 1
        
        return ans
