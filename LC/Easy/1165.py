class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indexes = defaultdict(int)
        
        for i, l in enumerate(keyboard):
            indexes[l] = i
            
        ans = 0
        temp = 0
        
        for c in word:
            ans += abs(temp - indexes[c])
            temp = indexes[c]
            
        return ans