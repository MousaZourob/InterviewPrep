class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        q = []
        ans = [0] * n
        
        for i in range(n):
            q.append(i)
        
        for c in deck:
            ans[q.pop(0)] = c
                
            if q:
                q.append(q.pop(0))
        
        return ans