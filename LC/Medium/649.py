class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = [i for i, x in enumerate(senate) if x == 'R']
        D = [i for i, x in enumerate(senate) if x == 'D']
        
        while R and D:
            r, d = R.pop(0), D.pop(0)
            if r < d:
                R += r + len(senate),
            else:
                D += d + len(senate),
        
        return R and 'Radiant' or 'Dire'