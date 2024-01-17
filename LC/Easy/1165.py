class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ans = 0
        prev = keyboard[0]
        
        keys = {c: i for i, c in enumerate(keyboard)}
        
        print(keys)
        
        for c in word:
            ans += abs(keys[c] - keys[prev])
            prev = c
        
        return ans