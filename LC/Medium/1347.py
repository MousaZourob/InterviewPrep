class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        
        for c in t:
            if count[c] > 0:
                count[c] -= 1
                        
        return sum(count.values())