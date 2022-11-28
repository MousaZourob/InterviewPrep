class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        
        for match in matches:
            if match[0] not in players:
                players[match[0]] = 0
            if match[1] not in players:
                players[match[1]] = 0
            players[match[1]] += 1
        
        ans = [[],[]]
        for p, l in players.items():
            if l == 0:
                ans[0].append(p)
            if l == 1:
                ans[1].append(p)
               
        ans[0].sort()
        ans[1].sort()
        return ans