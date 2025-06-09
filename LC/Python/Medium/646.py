class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans = 0
        
        prev = -inf
        for p in pairs:
            if p[0] > prev:
                prev = p[1]
                ans += 1
        return ans